"""
Document Processing Service

Converts a file into our domain Document model.
"""

from pathlib import Path

from ingestion.document_loader import DocumentLoader
from ingestion.text_chunker import TextChunker

from models.document import Document
from models.chunk import Chunk

from utils.logger import logger


class DocumentProcessor:

    def __init__(self):

        self.loader = DocumentLoader()
        self.chunker = TextChunker()

    # --------------------------------------------------

    def process(
        self,
        file_path,
        source_type
    ):

        logger.info(f"Processing : {file_path}")

        # ------------------------------
        # Load
        # ------------------------------

        documents = self.loader.load(file_path)

        # ------------------------------
        # Chunk
        # ------------------------------

        split_documents = self.chunker.split_documents(
            documents
        )

        # ------------------------------
        # Build Domain Model
        # ------------------------------

        path = Path(file_path)

        document = Document(

            name=path.name,

            source_type=source_type,

            file_type=path.suffix.lower()
        )

        # ------------------------------
        # Convert every split document
        # into our Chunk model
        # ------------------------------

        for index, item in enumerate(split_documents):

            chunk = Chunk(

                text=item.page_content,

                page=item.metadata.get(
                    "page",
                    0
                ),

                metadata={

                    **item.metadata,

                    "chunk_number": index,

                    "document_id": document.id,

                    "document_name": document.name,

                    "source_type": source_type

                }
            )

            document.chunks.append(chunk)

        logger.success(

            f"{document.name} processed into "
            f"{len(document.chunks)} chunks."

        )

        return document
