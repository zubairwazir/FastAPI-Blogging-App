from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_db
from app.config.hashing import HashPwd
from app.models.models import UserModel
from app.schemas.schemas import UserSchema, UserUpdateSchema, UserLoginSchema, UserResponseSchema


def create_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = UserModel(fname=user.fname, lname=user.lname, email=user.email, password=HashPwd.bcrypt(user.password),
                         age=user.age, is_active=user.is_active, is_admin=user.is_admin)

    if db.query(UserModel).filter(UserModel.email == user.email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{user.email} already exists!")

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} is not exists")
    return user
