from dataclasses import dataclass, field
from typing import Optional

from models.base_model import BaseModel


@dataclass
class Chunk(BaseModel):

    text: str = ""

    page: int = 0

    embedding: Optional[list] = None

    metadata: dict = field(default_factory=dict)