"""
Chroma Repository

Concrete implementation of DocumentRepository.
"""

from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

from config.settings import settings
from memory.search_result import RetrievedChunk, SearchResult
from repositories.document_repository import DocumentRepository
from utils.logger import logger


class ChromaRepository(DocumentRepository):

    def __init__(self, collection_name: str):

        logger.info(
            f"Initializing repository : {collection_name}"
        )

        self.client = PersistentClient(
            path=settings.CHROMA_DB_PATH
        )

        embedding_model = settings.get_sentence_transformer_model()

        self.embedding_function = SentenceTransformerEmbeddingFunction(
            model_name=embedding_model
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_function
        )

        logger.success(
            f"Collection '{collection_name}' ready."
        )

    # ------------------------------------------------

    def save(self, document):

        ids = []
        texts = []
        metadatas = []

        for chunk in document.chunks:

            ids.append(chunk.id)

            texts.append(chunk.text)

            metadatas.append(chunk.metadata)

        self.collection.add(

            ids=ids,

            documents=texts,

            metadatas=metadatas

        )

        logger.success(

            f"Stored {len(ids)} chunks "
            f"from {document.name}"

        )

    # ------------------------------------------------

    def search(
        self,
        query,
        top_k=5
    ):

        response = self.collection.query(

            query_texts=[query],

            n_results=top_k

        )

        result = SearchResult()

        documents = response.get(
            "documents",
            [[]]
        )[0]

        metadatas = response.get(
            "metadatas",
            [[]]
        )[0]

        distances = response.get(
            "distances",
            [[]]
        )[0]

        for text, metadata, distance in zip(

            documents,

            metadatas,

            distances

        ):

            result.chunks.append(

                RetrievedChunk(

                    text=text,

                    score=1 - distance,

                    metadata=metadata

                )

            )

        return result

    # ------------------------------------------------

    def delete(
        self,
        document_id
    ):

        self.collection.delete(

            where={
                "document_id": document_id
            }

        )

        logger.info(
            f"Deleted document {document_id}"
        )

    # ------------------------------------------------

    def count(self):

        return self.collection.count()
