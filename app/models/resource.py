#!/usr/bin/env python3
"""
Resource module for resource hub to be added
"""
from sqlalchemy import Column, Integer, String, Text
from models.base_model import Base


class Resource(Base):
    """
    Table for the Resources
    """
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    url = Column(String, unique=True)
    category = Column(String)
