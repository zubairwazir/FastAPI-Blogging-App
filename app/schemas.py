from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    fname: str
    lname: str
    email: str
    password: str
    age: int
    is_active: Optional[bool] = False
    is_admin: Optional[bool] = False


class UserUpdateSchema(BaseModel):
    fname: Optional[str]
    lname: Optional[str]
    password: Optional[str]
    age: Optional[int]


class UserLoginSchema(BaseModel):
    username: str
    password: str


class UserResponseSchema(BaseModel):
    fname: Optional[str]
    lname: Optional[str]
    email: Optional[str]
    age: Optional[int]

    class Config:
        orm_mode = True


class BlogSchema(BaseModel):
    id: int
    title: str
    description: str


class BlogUpdateSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]


class BlogResponseSchema(BaseModel):
    title: str
    description: str
