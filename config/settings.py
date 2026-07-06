"""
Application Settings

Loads environment variables and exposes them
through a single Settings class.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Load the project-local .env regardless of the launch directory.
load_dotenv(BASE_DIR / ".env")


class Settings:
    DEFAULT_SENTENCE_TRANSFORMER = "BAAI/bge-small-en-v1.5"

    BASE_DIR = BASE_DIR

    # =========================
    # LLM
    # =========================
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "llama-3.3-70b-versatile"
    )

    # =========================
    # Embeddings
    # =========================
    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        DEFAULT_SENTENCE_TRANSFORMER
    )

    # =========================
    # Vector Store
    # =========================
    CHROMA_DB_PATH = os.getenv(
        "CHROMA_DB_PATH",
        str(BASE_DIR / "vector_store")
    )

    STATIC_DB = os.getenv(
        "STATIC_DB",
        "static_db"
    )

    WEBSITE_DB = os.getenv(
        "WEBSITE_DB",
        "website_db"
    )

    UPLOAD_DB = os.getenv(
        "UPLOAD_DB",
        "upload_db"
    )

    DATA_DIR = BASE_DIR / "data"

    UPLOADS_DIR = DATA_DIR / "uploads"

    UPLOAD_INCOMING_DIR = UPLOADS_DIR / "incoming"

    UPLOAD_PROCESSED_DIR = UPLOADS_DIR / "processed"

    # =========================
    # Logging
    # =========================
    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    @classmethod
    def get_sentence_transformer_model(cls):
        embedding_model = cls.EMBEDDING_MODEL

        # OpenAI embedding ids cannot be loaded by SentenceTransformer.
        if embedding_model.startswith("text-embedding-"):
            return cls.DEFAULT_SENTENCE_TRANSFORMER

        return embedding_model


settings = Settings()
