#!/usr/bin/env python3
"""
User class for every user
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base_model import Base


class User(Base):
    """
    This is the User class inheriting from the Base
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(30), unique=True, index=True)
    hashed_password = Column(String(60))
    first_name = Column(String(20))
    last_name = Column(String(20))

    resources = relationship("Resource", back_populates="user")
    reviews = relationship("Review", back_populates="user")
    ratings = relationship("Rating", back_populates="user")
