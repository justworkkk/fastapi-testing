from datetime import datetime
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
