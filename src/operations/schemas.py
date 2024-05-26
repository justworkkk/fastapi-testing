from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class CurrencyEnum(str, Enum):
    Sell = "Sell"
    Buy = "Buy"


class OperationCreate(BaseModel):
    id: int
    currency: str
    quantity: str
    instrument_type: str
    date: datetime
    type: CurrencyEnum

    class Config:
        from_attributes = True


class ResponseModel(BaseModel):
    status: str
    data: Optional[List[OperationCreate]]
    details: Optional[str]
