#!/usr/bin/env python3
"""
This is the entry point of the application
"""
from fastapi import FastAPI
from app.routes import user
from app.models.user import Base
from app.config import DATABASE_URL
from sqlalchemy import create_engine

app = FastAPI()

# Database initialization
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/users", tags=["users"])


@app.get("/")
def read_root():
    """
    First return for root file
    """
    return {"message": "Welcome to the API"}
