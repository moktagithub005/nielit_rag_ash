"""
Base Ingestion Pipeline

Coordinates the complete document ingestion workflow.
"""

from ingestion.document_loader import DocumentLoader
from ingestion.text_chunker import TextChunker
from ingestion.metadata_manager import MetadataManager

from vector_store.chroma_manager import VectorStoreManager

from utils.logger import logger


class BaseIngestionPipeline:

    def __init__(self):

        self.loader = DocumentLoader()

        self.chunker = TextChunker()

        self.vector_store = VectorStoreManager()

    # ----------------------------------------------------

    def ingest(
        self,
        file_path,
        collection_name,
        source_type
    ):

        logger.info(f"Starting ingestion : {file_path}")

        # ------------------------------------
        # Step 1 : Load Document
        # ------------------------------------

        documents = self.loader.load(file_path)

        # ------------------------------------
        # Step 2 : Chunk Document
        # ------------------------------------

        chunks = self.chunker.split_documents(
            documents
        )

        # ------------------------------------
        # Step 3 : Create Processed Document
        # ------------------------------------

        processed_document = MetadataManager.create_processed_document(

            chunks=chunks,

            file_path=file_path,

            source_type=source_type
        )

        # ------------------------------------
        # Step 4 : Store in Chroma
        # ------------------------------------

        self.vector_store.add_documents(

            collection_name=collection_name,

            ids=[
                chunk.id
                for chunk in processed_document.chunks
            ],

            documents=[
                chunk.text
                for chunk in processed_document.chunks
            ],

            metadatas=[
                chunk.metadata
                for chunk in processed_document.chunks
            ]
        )

        logger.success(
            f"{processed_document.name} ingested successfully."
        )

        return processed_document
