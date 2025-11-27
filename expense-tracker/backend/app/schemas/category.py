from pydantic import BaseModel

class BaseCategory(BaseModel):
    name : str

class CreateCategory(BaseCategory):
    pass 

class ResponseCategory(BaseCategory):
    id : int
    
    class Config:
        orm_mode=True

        