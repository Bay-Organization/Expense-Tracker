from pydantic import BaseModel, EmailStr, Field, validator

class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(..., max_length=72)

    @validator("password")
    def validate_password(cls, v):
        if len(v.encode("utf-8")) > 72:
            raise ValueError("Password cannot exceed 72 bytes.")
        return v


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class ResponseUser(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
