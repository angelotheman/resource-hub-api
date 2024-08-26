#!/usr/bin/env python3
"""
Module for an enum class which adds predefined options
"""
from enum import Enum


class ResourceCategory(str, Enum):
    """
    Adds predefined options for the resource
    """
    EDUCATION = "education"
    TECHNOLOGY = "technology"
    HEALTH = "health"
    ENTERTAINMENT = "entertainment"
    SCIENCE = "science"
