from services.retrieval_service import RetrievalService
from services.source_builder import SourceBuilder
from services.context_builder import ContextBuilder
from llm.groq_client import GroqClient


class RAGService:

    def __init__(self):

        self.retriever = RetrievalService()

        self.source_builder = SourceBuilder()

        self.context_builder = ContextBuilder()

        self.llm = GroqClient()

    # ------------------------------------

    def ask(
        self,
        question,
        history=None
    ):

        retrieval = self.retriever.retrieve(question)

        context = self.context_builder.build(retrieval)

        answer = self.llm.generate(

            context=context,

            question=question,

            history=history

        )

        sources = self.source_builder.build(

            retrieval

        )

        return {

            "answer": answer,

            "sources": sources

        }

    # ------------------------------------

    def stream_ask(
        self,
        question,
        history=None
    ):

        retrieval = self.retriever.retrieve(question)

        context = self.context_builder.build(retrieval)

        sources = self.source_builder.build(

            retrieval

        )

        stream = self.llm.stream_generate(

            context=context,

            question=question,

            history=history

        )

        return {

            "stream": stream,

            "sources": sources

        }
