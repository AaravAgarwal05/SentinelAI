from pydantic import BaseModel, Field
from datetime import datetime, UTC

class RemediationRequest(BaseModel):

    service: str
    namespace: str
    action: str
    reason: str
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )