#!/usr/bin/env python3
"""
Routes for review
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app.models.review import Review
from app.schemas.review import ReviewCreate, ReviewOut
from app.models.user import User
from app.models.resource import Resource

router = APIRouter()


@router.post("/", response_model=ReviewOut)
def create_review(
        review: ReviewCreate, db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)):
    """
    Create a review
    """
    db_review = Review(**review.dict(), user_id=current_user.id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


@router.get("/{resource_id}", response_model=List[ReviewOut])
def get_reviews(resource_id: int, db: Session = Depends(get_db)):
    """
    Get every review
    """
    reviews = db.query(Review).filter(Review.resource_id == resource_id).all()
    return reviews
