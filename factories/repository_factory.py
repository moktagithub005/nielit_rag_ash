"""
Repository Factory
"""

from repositories.chroma_repository import ChromaRepository

from config.constants import (
    STATIC_COLLECTION,
    WEBSITE_COLLECTION,
    UPLOAD_COLLECTION
)


class RepositoryFactory:

    COLLECTIONS = {

        "static": STATIC_COLLECTION,

        "website": WEBSITE_COLLECTION,

        "upload": UPLOAD_COLLECTION

    }

    @classmethod
    def get_repository(
        cls,
        source_type
    ):

        collection = cls.COLLECTIONS[source_type]

        return ChromaRepository(
            collection_name=collection
        )