from pydantic import BaseModel
from datetime import datetime

class Incident(BaseModel):

    service: str

    severity: str

    event_type: str

    namespace: str

    message: str

    timestamp: datetime = datetime.utcnow()
