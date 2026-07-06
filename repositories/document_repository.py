"""
Abstract repository interface.

Every vector database implementation
must implement this interface.
"""

from abc import ABC, abstractmethod


class DocumentRepository(ABC):

    @abstractmethod
    def save(self, document):
        pass

    @abstractmethod
    def search(
        self,
        query,
        top_k=5
    ):
        pass

    @abstractmethod
    def delete(
        self,
        document_id
    ):
        pass

    @abstractmethod
    def count(self):
        pass
    