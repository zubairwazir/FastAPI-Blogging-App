from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_db
from app.schemas.schemas import BlogSchema, BlogUpdateSchema, BlogResponseSchema

from app.repository.blog import create, get, get_all, delete, update


router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=BlogResponseSchema)
def get_blog(id: int, db: Session = Depends(get_db)):
    return get(id, db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[BlogResponseSchema])
def get_all_blogs(db: Session = Depends(get_db)):
    return get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BlogResponseSchema)
def create_blog(blog: BlogSchema, db: Session = Depends(get_db)):
    return create(blog, db)


@router.put("/", status_code=status.HTTP_202_ACCEPTED, response_model=BlogResponseSchema)
def update_blog(id: int, blog: BlogUpdateSchema, db: Session = Depends(get_db)):
    return update(id, blog, db)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    return delete(id, db)



