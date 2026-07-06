"""
Metadata Manager
"""

import uuid
from pathlib import Path
from datetime import datetime

from models.chunk import Chunk
from models.document import Document


class MetadataManager:

    @staticmethod
    def create_processed_document(
        chunks,
        file_path,
        source_type
    ):

        path = Path(file_path)

        document_id = str(uuid.uuid4())

        document = Document(
            id=document_id,
            name=path.name,
            source_type=source_type,
            file_type=path.suffix.lower(),
            metadata={
                "document_id": document_id,
                "uploaded_at": datetime.now().isoformat()
            }
        )

        for index, chunk in enumerate(chunks):

            metadata = {

                "document_id": document_id,

                "document_name": path.name,

                "page": chunk.metadata.get("page", 0),

                "chunk_number": index,

                "source_type": source_type,

                "uploaded_at": datetime.now().isoformat(),

                "file_type": path.suffix.lower()

            }

            document.chunks.append(

                Chunk(

                    id=f"{document_id}_{index}",

                    text=chunk.page_content,

                    page=metadata["page"],

                    metadata=metadata

                )

            )

        return document
