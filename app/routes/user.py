#!/usr/bin/env python3
"""
Routing the user objects
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import (
        UserCreate, UserLogin, UserOut,
        PasswordResetRequest, PasswordReset
)
from app.schemas.resource import ResourceOut
from app.models.user import User
from app.auth.auth import (
        get_password_hash, verify_password,
        create_access_token, create_password_reset_token,
        verify_password_reset_token
)
from app.db import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.logger import setup_logger
from typing import List

router = APIRouter()
logger = setup_logger("user")


@router.get("/", response_model=List[UserOut])
def list_users(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)):
    """
    List all users
    """
    logger.info(f"Authenticated user: {current_user} accessed this resource"}
    users = db.query(User).all()
    return users


@router.get("/{user_id}/resources", response_model=List[ResourceOut])
def get_resources_for_user(
        user_id: int, db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)):
    """
    Get resources for a specific user
    """
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user.resources


@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user
    """
    logger.info(f"Attempting to register user with email: {user.email}")
    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user:
        logger.warning(
                f"Registration failed: Email already registered - \
                        {user.email}")
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)

    new_user = User(
        email=user.email,
        hashed_password=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    logger.info(f"User registered successfully: {user.email}")
    return new_user


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    """
    Login an existing user
    """
    logger.info(f"Login attempt for email: {user.email}")
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        logger.warning(f"Failed login attempt for email: {user.email}")
        raise HTTPException(status_code=400, detail="Invalid credentials")
    if not verify_password(user.password, db_user.hashed_password):
        logger.warning(f"Failed login attempt for email: {user.email}")
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": db_user.email})
    logger.info(f"User logged in successfully: {user.email}")
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/request-password-reset")
def request_password_reset(
        request: PasswordResetRequest,
        db: Session = Depends(get_db)):
    """
    Request for a password reset
    """
    logger.info(f"Password reset request for email: {request.email}")
    user = db.query(User).filter(User.email == request.email).first()

    if not user:
        logger.warning(f"Password reset request failed: User not found - \
                {request.email}")
        raise HTTPException(status_code=404, detail="User not found")

    reset_token = create_password_reset_token(user.id)
    logger.info(f"Password reset token generated for email: {request.email}")

    return {
        "message": "Password reset email sent",
        "reset_token": reset_token
    }


@router.post("/reset-password")
def reset_password(data: PasswordReset, db: Session = Depends(get_db)):
    """
    Reset the password
    """
    logger.info("Reset the password with this route")
    user_id = verify_password_reset_token(data.token)

    if not user_id:
        logger.warning(f"{user_id} not found")
        raise HTTPException(status_code=404, detail="Invalid or Expired token")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        logger.warning9(f"User - {user} not found")
        raise HTTPException(status_code=404, detail="User not found")

    user.hashed_password = get_password_hash(data.new_password)

    logger.info("Password reset successful")
    db.commit()

    return {"message": "Password updated successfully"}


@router.post("/logout")
def logout():
    """
    Invalidate the current user's token (on the client-side).
    """
    logger.info("Logout successful")
    return {
        "message": "Successfully logged out. Please \
                discard the token on the client-side."}
