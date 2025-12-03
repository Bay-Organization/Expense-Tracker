from pydantic import BaseModel
from datetime import date

class TransactionCreate(BaseModel):
    amount: float
    type: str
    description: str | None = None
    date: date
    category_id: int

class TransactionResponse(BaseModel):
    id: int
    amount: float
    type: str
    description: str | None
    date: date
    category_id: int

    class Config:
        orm_mode = True
