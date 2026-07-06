"""
Centralized ChromaDB Manager
"""

from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

from config.settings import settings
from utils.logger import logger


class VectorStoreManager:

    def __init__(self):

        logger.info("Initializing ChromaDB...")

        self.client = PersistentClient(
            path=settings.CHROMA_DB_PATH
        )

        self.embedding_function = SentenceTransformerEmbeddingFunction(
            model_name=settings.get_sentence_transformer_model()
        )

        logger.success("ChromaDB Initialized Successfully.")

    # -----------------------------------------------------

    def get_collection(self, collection_name):

        return self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_function
        )

    # -----------------------------------------------------

    def add_documents(
        self,
        collection_name,
        ids,
        documents,
        metadatas
    ):
        """
        Add documents into ChromaDB.
        """

        collection = self.get_collection(collection_name)

        collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )

        logger.success(
            f"{len(documents)} documents added to {collection_name}"
        )

    # -----------------------------------------------------

    def similarity_search(
        self,
        collection_name,
        query,
        top_k=5
    ):
        """
        Search similar documents.
        """

        collection = self.get_collection(collection_name)

        results = collection.query(
            query_texts=[query],
            n_results=top_k
        )

        return results

    # -----------------------------------------------------

    def delete_documents(
        self,
        collection_name,
        ids
    ):

        collection = self.get_collection(collection_name)

        collection.delete(ids=ids)

        logger.info(
            f"Deleted {len(ids)} documents."
        )

    # -----------------------------------------------------

    def get_document_count(
        self,
        collection_name
    ):

        collection = self.get_collection(collection_name)

        return collection.count()

    # -----------------------------------------------------

    def reset_collection(
        self,
        collection_name
    ):

        self.client.delete_collection(collection_name)

        logger.warning(
            f"{collection_name} deleted."
        )
