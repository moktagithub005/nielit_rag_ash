from llm.rag_service import RAGService


class ChatController:

    def __init__(self):

        self.rag = RAGService()

    # -----------------------------

    def ask(self, question):

        return self.rag.ask(question)

    # -----------------------------

    def stream_ask(
        self,
        question,
        history=None
    ):

        return self.rag.stream_ask(
            question=question,
            history=history
        )
