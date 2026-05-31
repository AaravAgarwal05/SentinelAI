from pydantic import BaseModel, Field
from datetime import datetime, UTC

class Incident(BaseModel):

    service: str
    severity: str
    event_type: str
    namespace: str
    message: str

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )