from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    email: str


class Book(BaseModel):
    bookID: str
    bookName: str
    author: str
