from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email:EmailStr
    password:str


class User(BaseModel):
    id:int
    email:EmailStr
    class Config():
        orm_mode=True


class NoteUpload(BaseModel):
    filename:str

class Note(NoteUpload):
    id:int
    content:str
    user:User
    class Config():
        orm_mode=True

class Login(BaseModel):
    username:EmailStr
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str | None = None