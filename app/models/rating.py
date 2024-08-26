#!/usr/bin/env python3
"""
Rating table in this module
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base_model import Base


class Rating(Base):
    """
    Ratings for every resource by user
    """
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))

    user = relationship("User", back_populates="ratings")
    resource = relationship("Resource", back_populates="ratings")
