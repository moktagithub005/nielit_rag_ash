from dataclasses import dataclass, field
from typing import List

from models.base_model import BaseModel
from models.chunk import Chunk


@dataclass
class Document(BaseModel):

    name: str = ""

    source_type: str = ""

    file_type: str = ""

    metadata: dict = field(default_factory=dict)

    chunks: List[Chunk] = field(default_factory=list)