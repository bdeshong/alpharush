from pydantic import BaseModel
from datetime import datetime

class PhraseBase(BaseModel):
    phrase: str

class PhraseResponse(PhraseBase):
    uuid: str
    created: datetime
    last_updated: datetime

    class Config:
        from_attributes = True
