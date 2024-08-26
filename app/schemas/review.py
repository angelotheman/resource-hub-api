#!/usr/bin/env python3
"""
Reviews for resources module
"""
from pydantic import BaseModel


class ReviewBase(BaseModel):
    """
    Validate foundation for review
    """
    text: str


class ReviewCreate(ReviewBase):
    """
    Validate creating of review
    """
    pass


class ReviewOut(ReviewBase):
    """
    Validate review
    """
    id: int
    user_id: int
    resource_id: int

    class Config:
        orm_mode = True
