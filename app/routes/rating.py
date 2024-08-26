#!/usr/bin/env python3
"""
Rating module routes
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app.models.rating import Rating
from app.schemas.rating import RatingCreate, RatingOut
from app.models.user import User
from app.models.resource import Resource

router = APIRouter()


@router.post("/", response_model=RatingOut)
def create_rating(
        rating: RatingCreate, db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)):
    """
    Create a new rating
    """
    db_rating = Rating(**rating.dict(), user_id=current_user.id)
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating


@router.get("/{resource_id}", response_model=List[RatingOut])
def get_ratings(resource_id: int, db: Session = Depends(get_db)):
    """
    Get number of ratings on an id
    """
    ratings = db.query(Rating).filter(Rating.resource_id == resource_id).all()
    return ratings
