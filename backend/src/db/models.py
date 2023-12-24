from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class User(Base):

    __tablename__ = "users"

    # Columns
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String) # Of course, the password is gonna be hashed
    is_active = Column(Boolean, default=True)


