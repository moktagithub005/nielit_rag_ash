"""
Domain model representing a document.

This class is independent of LangChain.
"""

from dataclasses import dataclass


@dataclass
class AppDocument:

    text: str

    metadata: dict

