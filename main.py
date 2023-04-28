from fastapi_offline import FastAPIOffline as FastAPI
from typing import List
from fastapi import Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from app.config import HashPwd
from app.database import engine, get_db
from app.models import Base, UserModel, BlogModel
from app.schemas import UserSchema, UserUpdateSchema, UserLoginSchema, UserResponseSchema, BlogSchema, BlogUpdateSchema, BlogResponseSchema

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.post("/register_user", status_code=status.HTTP_201_CREATED)
def register_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = UserModel(fname=user.fname, lname=user.lname, email=user.email, password=HashPwd.bcrypt(user.password),
                         age=user.age, is_active=user.is_active, is_admin=user.is_admin)

    if db.query(UserModel).filter(UserModel.email == user.email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{user.email} already exists!")

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/login_user")
def login_user(user: UserLoginSchema, db: Session = Depends(get_db)):
    return {"User": "Logged In"}


@app.get("/get_user/{id}", status_code=status.HTTP_200_OK, response_model=UserResponseSchema)
def get_user(id: int, response: Response, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} is not exists")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"user with id {id} is not exists"}
    return user


@app.put("/update_user/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_user(id: int, user: UserUpdateSchema, db: Session = Depends(get_db)):
    update_user = db.query(UserModel).filter(UserModel.id == id)
    if not update_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id{id} not exists!")
    update_user.update(user)
    db.commit()
    return "Updated!"


@app.delete("/delete_user", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with id {id} not Found!")

    user.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"User with id {id} is deleted!"}


@app.get("/get_all_users", status_code=status.HTTP_200_OK, response_model=List[UserResponseSchema])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Users found!")
    return users


@app.post("/create_blog", status_code=status.HTTP_201_CREATED, response_model=BlogResponseSchema)
def create_blog(blog: BlogSchema, db: Session = Depends(get_db)):
    new_blog = BlogModel(title=blog.title, description=blog.description)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/get_blog/{id}", status_code=status.HTTP_200_OK, response_model=BlogResponseSchema)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No Blog with id {id} Found!")

    return blog


@app.get("/get_blogs", status_code=status.HTTP_200_OK, response_model=BlogResponseSchema)
def get_blog(id: int, db: Session = Depends(get_db)):
    blogs = db.query(BlogModel).all()

    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Blog Found!")

    return blogs
