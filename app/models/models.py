from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    age = Column(Integer)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

    blogs = relationship("BlogModel", back_populates='author')

    def __repr__(self):
        return f"<User {self.email}"


class BlogModel(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("UserModel", back_populates='blogs')

