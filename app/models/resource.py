#!/usr/bin/env python3
"""
Resource module for resource hub to be added
"""
from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import Base
from app.models.category import ResourceCategory


class Resource(Base):
    """
    Table for the Resources
    """
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, index=True)
    description = Column(Text)
    url = Column(String(126), unique=True)
    category = Column(Enum(ResourceCategory), nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="resources")
    reviews = relationship("Review", back_populates="resource")
    ratings = relationship("Rating", back_populates="resource")
