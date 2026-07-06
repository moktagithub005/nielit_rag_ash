"""
Search Result Domain Model
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class RetrievedChunk:

    text: str

    score: float

    metadata: dict


@dataclass
class SearchResult:

    chunks: List[RetrievedChunk] = field(default_factory=list)