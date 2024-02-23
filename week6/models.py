from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = "User"

    userID = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, index=True)
    firstName = Column(String(50))
    lastName = Column(String(50))
