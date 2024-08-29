#!/usr/bin/env python3
"""
This is the entry point of the application
"""
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from app.routes import (
        user, resource,
        review, rating
)
from app.models.user import Base
from app.config import DATABASE_URL
from sqlalchemy import create_engine
from app.logger import setup_logger


app = FastAPI()
logger = setup_logger("main")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

# Routers to various parts of the app
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(resource.router, prefix="/resources", tags=["resources"])
app.include_router(review.router, prefix="/reviews", tags=["reviews"])
app.include_router(rating.router, prefix="/ratings", tags=["ratings"])


@app.on_event("startup")
async def startup_event():
    logger.info("Application is starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application is shutting down...")


@app.get("/")
def read_root():
    """
    First return for root file
    """
    return {"message": "Welcome to the API"}
