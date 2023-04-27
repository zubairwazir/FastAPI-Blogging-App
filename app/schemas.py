from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    fname: str
    lname: str
    email: str
    password: str
    age: int
    is_active: Optional[bool]
    is_admin: Optional[bool]


class UserUpdateSchema(BaseModel):
    fname: Optional[str]
    lname: Optional[str]
    password: Optional[str]
    age: Optional[int]


class UserLoginSchema(BaseModel):
    username: str
    password: str


class UserR
