from dataclasses import dataclass


@dataclass
class IngestionReport:

    files_found: int = 0

    files_processed: int = 0

    files_skipped: int = 0

    total_chunks: int = 0

    processing_time: float = 0