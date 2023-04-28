from pydantic import BaseModel
from typing import Optional, List


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


class BlogSchema(BaseModel):
    title: str
    description: str


class GetBlogsSchema(BlogSchema):
    class Config:
        orm_mode = True


class BlogUpdateSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]


class UserResponseSchema(BaseModel):
    fname: Optional[str]
    lname: Optional[str]
    email: Optional[str]
    age: Optional[int]
    blogs: List[GetBlogsSchema] = []

    class Config:
        orm_mode = True


class BlogResponseSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]
    author: UserResponseSchema = None

    class Config:
        orm_mode = True
