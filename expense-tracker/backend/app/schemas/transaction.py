from pydantic import BaseModel, ConfigDict
from datetime import date

class BaseTransaction(BaseModel):
    amount : float
    type : str
    description : str | None = None
    date  : date
    category_id : int

class CreateTransaction(BaseTransaction):
    pass

class ResponseTransaction(BaseTransaction):
    id : int
    user_id : int

    class Config:
        model_config = ConfigDict(from_attributes=True)
