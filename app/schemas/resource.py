#!/usr/bin/env python3
"""
Schema for the resource module
"""
from pydantic import BaseModel
from app.models.category import ResourceCategory


class ResourceBase(BaseModel):
    """
    Validates the basic structure of resource
    """
    name: str
    description: str
    url: str
    category: ResourceCategory


class ResourceOut(ResourceBase):
    """
    Checks to delete a resource
    """
    id: int
    user_id: int

    class Config:
        """
        Checks the exact config for this
        """
        from_attributes = True


class ResourceCreate(ResourceBase):
    """
    Validates the creation of a resource
    """
    user_id: int
