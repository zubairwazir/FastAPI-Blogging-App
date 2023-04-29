from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.config.hashing import HashPassword
from app.models.models import UserModel
from app.schemas.schemas import UserLoginSchema


router = APIRouter(
    tags=['Auth']
)


@router.post('/login')
def login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    get_user = db.query(UserModel).filter(UserModel.email == user.username).first()

    if not get_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    if not HashPassword.verify(user.password, get_user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")

    return get_user
