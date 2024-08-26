#!/usr/bin/env python3
"""
Resource Module for the resources to be used
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.resource import Resource
from app.models.user import User
from app.schemas.resource import ResourceCreate, ResourceOut
from app.db import get_db
from typing import List

router = APIRouter()


@router.get("/", response_model=List[ResourceOut])
def list_resources(db: Session = Depends(get_db)):
    """
    List all the available resources
    """
    resources = db.query(Resource).all()

    return resources


@router.get("/{resource_id}", response_model=ResourceOut)
def get_resource(resource_id: int, db: Session = Depends(get_db)):
    """
    Get a single resource
    """
    resource = db.query(Resource).filter(Resource.id == resource.id).first()

    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")

    return resource


@router.post("/", response_model=ResourceOut)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    """
    Creates a new resource
    """
    db_resource = db.query(Resource).filter(
            Resource.name == resource.name).first()

    if db_resource:
        raise HTTPException(status_code=400, detail="Resource already exists")

    new_resource = Resource(**resource.dict())

    db.add(new_resource)
    db.commit()
    db.refresh(new_resource)

    return new_resource


@router.put("/{resource_id}", response_model=ResourceOut)
def update_resource(resource_id: int, resource: ResourceCreate,
                    db: Session = Depends(get_db)):
    """
    Update the resource by the id
    """
    db_resource = db.query(Resource).filter(Resource.id == resource.id).first()

    if not db_resource:
        raise HTTPException(status_code=404, detail="Resource not found")

    db_resource.name = resource.name
    db_resource.description = resource.description
    db_resource.url = resource.url
    db_resource.category = resource.category

    db.commit()
    db.refresh(db_resource)

    return db_resource


@router.delete("/{resource_id}")
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    """
    Delete a resource by ID
    """
    resource = db.query(Resource).filter(Resource.id == resource_id).first()

    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")

    db.delete(resource)
    db.commit()

    return {"message": "Resource deleted successfully"}
