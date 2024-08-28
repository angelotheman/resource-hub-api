#!/usr/bin/env python3
"""
Rating module
"""
from pydantic import BaseModel


class RatingBase(BaseModel):
    """
    Rating validation
    """
    value: int


class RatingCreate(RatingBase):
    """
    Validate rating creation
    """
    pass


class RatingOut(RatingBase):
    """
    Validate ratings out
    """
    id: int
    user_id: int
    resource_id: int

    class Config:
        from_attributes = True
