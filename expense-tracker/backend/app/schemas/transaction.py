from pydantic import BaseModel
from datetime import date

class TransactionBase(BaseModel):
    amount : float
    type : str
    description : str | None = None
    date : date
    category_id : int

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id : int 
    user_id : int 