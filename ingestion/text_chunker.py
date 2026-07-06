"""
Text Chunker

Splits LangChain Documents into smaller chunks.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.constants import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

from utils.logger import logger


class TextChunker:

    def __init__(
        self,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    ):
        """
        Initialize the text splitter.
        """

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

        logger.info(
            f"TextChunker initialized "
            f"(chunk_size={self.chunk_size}, "
            f"chunk_overlap={self.chunk_overlap})"
        )

    # --------------------------------------------------

    def split_documents(self, documents):
        """
        Split LangChain Documents into smaller chunks.
        """

        logger.info(
            f"Splitting {len(documents)} document(s)..."
        )

        chunks = self.splitter.split_documents(
            documents
        )

        logger.success(
            f"Generated {len(chunks)} chunks."
        )

        return chunks