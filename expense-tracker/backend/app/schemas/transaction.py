from pydantic import BaseModel

class TransactionBase(BaseModel):
    amount : float
class TransactionCreate(TransactionBase):

class TransactionResponse(TransactionBase):