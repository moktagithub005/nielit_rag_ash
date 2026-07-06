"""
Base model for all domain entities.
"""

from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass
class BaseModel:

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )