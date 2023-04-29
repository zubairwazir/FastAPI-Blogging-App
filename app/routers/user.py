from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from app.config.database import get_db
from app.repository.user import get, get_all, create, update, delete, login
from app.schemas.schemas import UserSchema, UserUpdateSchema, UserLoginSchema, UserResponseSchema


router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UserResponseSchema)
def get_user(id: int, db: Session = Depends(get_db)):
    return get(id, db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[UserResponseSchema])
def get_all_users(db: Session = Depends(get_db)):
    return get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponseSchema)
def register_user(user: UserSchema, db: Session = Depends(get_db)):
    return create(user, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=UserResponseSchema)
def update_user(id: int, user: UserUpdateSchema, db: Session = Depends(get_db)):
    return update(id, user, db)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    return delete(id, db)


@router.post("/")
def login_user(user: UserLoginSchema, db: Session = Depends(get_db)):
    return login(user, db)

