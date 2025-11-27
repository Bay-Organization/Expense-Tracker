from fastapi import FastAPI
from .database import engine,Base
from app import models
from app.routers import auth

app = FastAPI()

Base.metadata.create_all(bind = engine)

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Expense Tracker API is running"}