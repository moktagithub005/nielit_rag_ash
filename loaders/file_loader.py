from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredExcelLoader,
)

from loaders.base_loader import BaseLoader
from models.app_document import AppDocument
from utils.logger import logger


class FileLoader(BaseLoader):

    def load(self, file_path):

        path = Path(file_path)

        suffix = path.suffix.lower()

        if suffix == ".pdf":
            loader = PyPDFLoader(file_path)

        elif suffix == ".docx":
            loader = UnstructuredWordDocumentLoader(file_path)

        elif suffix == ".txt":
            loader = TextLoader(file_path)

        elif suffix == ".xlsx":
            loader = UnstructuredExcelLoader(file_path)

        else:
            raise ValueError(f"Unsupported file type: {suffix}")

        documents = loader.load()

        result = []

        for doc in documents:
            result.append(
                AppDocument(
                    text=doc.page_content,
                    metadata=doc.metadata
                )
            )

        logger.success(f"Loaded {len(result)} document(s).")

        return result