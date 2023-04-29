from fastapi import status, HTTPException
from app.config.hashing import HashPassword
from app.models.models import UserModel


def get(id, db):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} is not exists")
    return user


def get_all(db):
    users = db.query(UserModel).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Users found!")
    return users


def create(user, db):
    new_user = UserModel(fname=user.fname, lname=user.lname, email=user.email, password=HashPassword.bcrypt(user.password),
                         age=user.age, is_active=user.is_active, is_admin=user.is_admin)

    if db.query(UserModel).filter(UserModel.email == user.email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{user.email} already exists!")

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update(id, user, db):
    get_user = get(id, db)
    if not get_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id{id} not exists!")

    get_user.update(user)
    db.commit()
    return {"detail": f"User with id {id} is updated!"}


def delete(id, db):
    get_user = get(id, db)
    if not get_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with id {id} not Found!")

    get_user.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"User with id {id} is deleted!"}


def login(db):
    pass
