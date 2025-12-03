from pydantic import BaseModel, EmailStr
from pydantic import ConfigDict

class BaseUser(BaseModel):
    username : str
    email : EmailStr

class CreateUser(BaseUser):
    password : str

class LoginUser(BaseModel):
    email: str
    password: str

class ResponseUser(BaseUser):
    id : int 
    
    class Config:
        model_config = ConfigDict(from_attributes=True)
   