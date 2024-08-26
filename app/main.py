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

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

# Routers to various parts of the app
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(resource.router, prefix="/resources", tags=["resources"])


@app.get("/")
def read_root():
    """
    First return for root file
    """
    return {"message": "Welcome to the API"}
