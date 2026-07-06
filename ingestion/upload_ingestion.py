from config.constants import UPLOAD_COLLECTION
from ingestion.base_ingestion import BaseIngestionPipeline


class UploadIngestionPipeline(BaseIngestionPipeline):

    def ingest_file(self, file_path):

        return self.ingest(
            file_path=file_path,
            collection_name=UPLOAD_COLLECTION,
            source_type="upload"
        )
