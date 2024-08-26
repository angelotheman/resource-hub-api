#!/usr/bin/env python3
"""
Security, Authentication and Authorization
"""
from passlib.context import CryptContext
from typing import Union
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    """
    Secure getting password
    """
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """
    Verify the password
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    """
    Create the access token
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_password_reset_token(user_id: int) -> str:
    """
    Create a password reset JWT token
    """
    data = {"sub": user_id}
    return create_access_token(data, expires_delta=timedelta(hours=1))


def verify_password_reset_token(token: str) -> Union[int, None]:
    """
    Verify a password reset token
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload.get("sub")
    except JWTError:
        return None
