"""
Loads documents of different file formats.
"""

from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredExcelLoader
)

from utils.logger import logger
from langchain_core.documents import Document as AppDocument


class DocumentLoader:

    @staticmethod
    def load(file_path):
        """
        Automatically loads a supported document.
        """

        path = Path(file_path)

        suffix = path.suffix.lower()

        logger.info(f"Loading {path.name}")

        if suffix == ".pdf":
            loader = PyPDFLoader(file_path)

        elif suffix == ".docx":
            loader = UnstructuredWordDocumentLoader(file_path)

        elif suffix == ".txt":
            loader = TextLoader(file_path)

        elif suffix == ".xlsx":
            loader = UnstructuredExcelLoader(file_path)

        else:
            raise ValueError(
                f"Unsupported file type : {suffix}"
            )

        loaded_docs = loader.load()

        documents = []

        for doc in loaded_docs:
            documents.append(
                AppDocument(
                    page_content=doc.page_content,
                    metadata=doc.metadata,
                )
            )

        logger.success(f"{len(documents)} document(s) loaded.")

        return documents