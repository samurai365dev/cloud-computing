from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    firstName: str
    lastName: str


class User(UserBase):
    userID: int
    firstName: str
    lastName: str

    class Config:
        orm_mode = True
