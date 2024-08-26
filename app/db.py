#!/usr/bin/env python3
"""
Database setup and session management
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Dependency for providing a database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
