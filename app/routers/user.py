from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_db
from app.config.hashing import HashPwd
from app.models.models import UserModel
from app.schemas.schemas import UserSchema, UserUpdateSchema, UserLoginSchema, UserResponseSchema
from app.repository.user import create_user


router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponseSchema)
def register_user(user: UserSchema, db: Session = Depends(get_db)):
    return create_user()


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UserResponseSchema)
def get_user(id: int, db: Session = Depends(get_db)):
    return get_user(id)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=UserResponseSchema)
def update_user(id: int, user: UserUpdateSchema, db: Session = Depends(get_db)):
    update_user = db.query(UserModel).filter(UserModel.id == id).first()
    if not update_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id{id} not exists!")
    update_user.update(user)
    db.commit()
    return {"detail": f"User with id {id} is updated!"}


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with id {id} not Found!")

    user.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"User with id {id} is deleted!"}


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[UserResponseSchema])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Users found!")
    return users


@router.post("/")
def login_user(user: UserLoginSchema, db: Session = Depends(get_db)):
    return {"User": "Logged In"}

