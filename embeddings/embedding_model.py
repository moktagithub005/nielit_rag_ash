"""
Embedding Model
Loads the Sentence Transformer only once.
"""

from sentence_transformers import SentenceTransformer

from config.settings import settings
from utils.logger import logger


class EmbeddingModel:
    """
    Singleton wrapper around SentenceTransformer.
    """

    _model = None

    @classmethod
    def get_model(cls):
        """
        Returns the embedding model.
        Loads it only the first time.
        """

        if cls._model is None:

            logger.info(
                "Loading embedding model : "
                f"{settings.get_sentence_transformer_model()}"
            )

            cls._model = SentenceTransformer(
                settings.get_sentence_transformer_model()
            )

            logger.success("Embedding model loaded successfully.")

        return cls._model
