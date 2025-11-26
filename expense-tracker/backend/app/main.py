from fastapi import FastAPI
from .database import engine,Base
from app import models

app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.get("/")
def root():
    return {"message": "Expense Tracker API is running"}