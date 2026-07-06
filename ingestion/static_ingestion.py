from pathlib import Path

from config.constants import STATIC_COLLECTION, SUPPORTED_EXTENSIONS
from ingestion.base_ingestion import BaseIngestionPipeline
from utils.logger import logger


class StaticIngestionPipeline(BaseIngestionPipeline):

    def __init__(self, source_dir=None):
        super().__init__()

        if source_dir is None:
            source_dir = (
                Path(__file__).resolve().parent.parent
                / "data"
                / "static"
                / "docs"
            )

        self.source_dir = Path(source_dir)

    def _collect_supported_files(self, directory):
        directory = Path(directory)

        if not directory.exists():
            return []

        supported_files = []

        for file_path in sorted(
            directory.rglob("*"),
            key=lambda path: (len(path.relative_to(directory).parts), str(path)),
        ):
            if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
                supported_files.append(file_path)

        return supported_files

    def ingest_directory(self, directory=None):
        source_dir = Path(directory or self.source_dir)

        files_to_ingest = self._collect_supported_files(source_dir)

        if not files_to_ingest:
            logger.warning(f"No supported static files found in {source_dir}")
            return []

        processed_documents = []

        for file_path in files_to_ingest:
            try:
                processed_document = self.ingest(
                    file_path=str(file_path),
                    collection_name=STATIC_COLLECTION,
                    source_type="static"
                )
                processed_documents.append(processed_document)
            except Exception as exc:
                logger.exception(f"Failed to ingest {file_path}: {exc}")

        logger.success(
            f"Completed static ingestion for {len(processed_documents)} document(s)."
        )

        return processed_documents

