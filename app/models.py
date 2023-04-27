from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean


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

    def __repr__(self):
        return f"<User {self.email}"
