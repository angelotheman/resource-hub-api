#!/usr/bin/env python3
"""
Routing the user objects
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.models.user import User
from app.utils.security import get_password_hash, verify_password
from app.utils.security import create_access_token
from app.db import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List

router = APIRouter()


@router.get("/", response_model=List[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    """
    List all users
    """
    users = db.query(User).all()
    return users


@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user
    """
    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user:
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
    return new_user


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    """
    Login an existing user
    """
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/request-password-reset")
def request_password_reset(
        request: schemas.PasswordResetRequest,
        db: Session = Depends(get_db)):
    """
    Request for a password reset
    """
    user = db.query(User).filter(User.email == request.email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    reset_token = create_password_reset_token(user.id)

    return {
        "msg": "Password reset email sent",
        "reset_token": reset_token
    }


@router.post("/reset-password")
def reset_password(data: Schemas.PasswordReset, db: Session = Depends(get_db)):
    """
    Reset the password
    """
    user_id = verify_password_reset_token(data.token)

    if not user_id:
        raise HTTPException(status_code=404, detail="Invalid or Expired token")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.hashed_password = hash_password(data.new_password)

    db.commit()

    return {"msg": "Password updated successfully"}
