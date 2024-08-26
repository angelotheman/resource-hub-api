#!/usr/bin/env python3
"""
Schemas for the user class
"""
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """
    Userbase class
    """
    email: EmailStr


class UserCreate(UserBase):
    """
    UserCreate Class
    """
    password: str
    first_name: str
    last_name: str


class UserOut(UserBase):
    """
    User Logout
    """
    id: int
    first_name: str
    last_name: str

    class Config:
        """
        Configure custom pydantic model
        """
        from_attributes = True


class UserLogin(BaseModel):
    """
    User Login
    """
    email: EmailStr
    password: str


class PasswordResetRequest(BaseModel):
    """
    Request for Password Reset
    """
    email: EmailStr


class PasswordReset(BaseModel):
    """
    Actual Password reset
    """
    token: str
    new_password: str
