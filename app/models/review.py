#!/usr/bin/env python3
"""
A module for the reviews
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.models.base_model import Base


class Review(Base):
    """
    Record every review given to a resource
    """
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))

    user = relationship("User", back_populates="reviews")
    resource = relationship("Resource", back_populates="reviews")
