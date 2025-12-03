from fastapi import FastAPI, Depends
from app.database import engine, Base
from app import models

from app.routers import auth
from app.routers import categories
from app.routers import transactions
from app.routers import summary

from app.utils.deps import get_current_user
from app.models.user import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(transactions.router)
app.include_router(summary.router)

@app.get("/")
def root():
    return {"message": "Expense Tracker API is running 🚀"}

@app.get("/me")
def read_me(user: User = Depends(get_current_user)):
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }