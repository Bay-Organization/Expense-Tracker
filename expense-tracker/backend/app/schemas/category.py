from pydantic import BaseModel, ConfigDict

class BaseCategory(BaseModel):
    name : str

class CreateCategory(BaseCategory):
    pass 

class ResponseCategory(BaseCategory):
    id : int
    
    class Config:
        model_config = ConfigDict(from_attributes=True)
        