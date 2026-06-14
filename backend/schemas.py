from pydantic import BaseModel
from datetime import date

class EntryCreate(BaseModel):
    title: str
    content: str
    date: date

class EntryResponse(BaseModel):
    id: int
    title: str
    content: str
    date: date

    class Config:
        from_attributes = True