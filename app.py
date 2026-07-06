import base64

import streamlit as st
import streamlit.components.v1 as components

from memory.memory_manager import MemoryManager
from services.tts_service import TextToSpeechService
from utils.file_utils import move_to_processed, save_uploaded_file


st.set_page_config(
    page_title="NIELIT AI Assistant",
    layout="wide",
)


@st.cache_resource(show_spinner=False)
def get_controller():
    from controllers.chat_controller import ChatController

    return ChatController()


@st.cache_resource(show_spinner=False)
def get_upload_pipeline():
    from ingestion.upload_ingestion import UploadIngestionPipeline

    return UploadIngestionPipeline()


@st.cache_resource(show_spinner=False)
def get_static_pipeline():
    from ingestion.static_ingestion import StaticIngestionPipeline

    return StaticIngestionPipeline()


def render_sources(sources):
    if not sources:
        st.caption("No sources returned.")
        return

    st.divider()
    st.caption("Sources")

    for source in sources:
        st.write(
            f"**{source['document']}** "
            f"(Page {source['page']}) "
            f"- Score: {source['score']}"
        )


def play_answer_audio(answer_text):
    try:
        tts_service = TextToSpeechService()
        audio_path = tts_service.synthesize(
            answer_text,
            output_path="output/assistant_reply.mp3",
        )

        with open(audio_path, "rb") as audio_file:
            audio_bytes = audio_file.read()

        encoded_audio = base64.b64encode(audio_bytes).decode("utf-8")
        html = f"""
        <audio autoplay controls style="display:none;">
            <source src="data:audio/mp3;base64,{encoded_audio}" type="audio/mpeg">
        </audio>
        """
        components.html(html, height=0)
    except Exception as exc:
        st.caption(f"Audio playback unavailable: {exc}")


def main():
    st.title("NIELIT AI Assistant")

    controller = None
    upload_pipeline = None
    static_pipeline = None
    backend_error = None

    try:
        controller = get_controller()
        upload_pipeline = get_upload_pipeline()
        static_pipeline = get_static_pipeline()
    except Exception as exc:
        backend_error = exc

    with st.sidebar:
        st.header("Admin Tools")

        if backend_error:
            st.error(f"Backend unavailable: {backend_error}")
            st.caption(
                "Install the missing dependencies and confirm your "
                "vector store / model configuration."
            )
        else:
            st.success("Backend ready")

        uploaded_pdf = st.file_uploader(
            "Upload a PDF for instant indexing",
            type=["pdf"],
            disabled=upload_pipeline is None,
        )

        if st.button(
            "Index Uploaded PDF",
            use_container_width=True,
            disabled=upload_pipeline is None,
        ):
            if uploaded_pdf is None:
                st.warning("Choose a PDF before indexing.")
            else:
                with st.spinner("Saving and indexing PDF..."):
                    saved_file = save_uploaded_file(uploaded_pdf)
                    processed_document = upload_pipeline.ingest_file(
                        str(saved_file)
                    )
                    move_to_processed(saved_file)

                st.success(
                    f"Indexed {processed_document.name} "
                    f"with {len(processed_document.chunks)} chunks."
                )

        if st.button(
            "Build Static Knowledge Base",
            use_container_width=True,
            disabled=static_pipeline is None,
        ):
            with st.spinner("Indexing static knowledge base..."):
                processed_documents = static_pipeline.ingest_directory()

            if processed_documents:
                st.success(
                    f"Indexed {len(processed_documents)} static document(s)."
                )
            else:
                st.info("No supported static documents were found to index.")

    chat_messages = MemoryManager.get_chat_messages()

    for message in chat_messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

            if message["role"] == "assistant":
                render_sources(message.get("sources"))

    if backend_error:
        st.info(
            "The UI is up, but the MVP backend is not ready yet. "
            "See the sidebar error for the missing piece."
        )
        return

    question = st.chat_input("Ask your question...")

    if not question:
        return

    history = MemoryManager.get_history()
    MemoryManager.add_user_message(question)

    with st.chat_message("user"):
        st.write(question)

    response = controller.stream_ask(
        question=question,
        history=history,
    )

    with st.chat_message("assistant"):
        answer = st.write_stream(response["stream"])
        render_sources(response["sources"])

        if answer:
            play_answer_audio(answer)

    MemoryManager.add_assistant_message(
        content=answer,
        sources=response["sources"],
    )


if __name__ == "__main__":
    main()
