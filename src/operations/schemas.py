from datetime import datetime
from typing import List
from pydantic import BaseModel


class OperationCreate(BaseModel):
    id: int
    currency: str
    quantity: str
    instrument_type: str
    date: datetime
    type: str

    class Config:
        orm_mode = True
        from_attributes = True


class ResponseModel(BaseModel):
    status: str
    data: List[OperationCreate]
    details: str
