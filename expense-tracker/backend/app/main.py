from fastapi import FastAPI
from app.database import engine,Base
from app import models
from fastapi import Depends
from app.utils.deps import get_current_user
from app.models.user import User
from app.routers import auth

app = FastAPI()

Base.metadata.create_all(bind = engine)

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Expense Tracker API is running"}

@app.get("/me")
def read_me(user: User = Depends(get_current_user)):
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }