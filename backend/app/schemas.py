from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

from pydantic import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    destination_id: int
    pass

class UserOut(BaseModel):
    id: int
    nickname: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode=True


class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode=True  

class Destination(BaseModel):
    name: str

class DestCreate(Destination):
    pass

class DestOut(DestCreate):
    id: int
    name: str
    
    class Config:
        orm_mode=True

class PostOut(BaseModel):
    Post: Post
    votes: int
    owner: UserOut
    dest: DestOut

    class Config:
        orm_mode=True 
    

class UserCreate(BaseModel):
    email: EmailStr
    nickname: str
    password: str



class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
'''
class PostUpdate(BaseModel):
    title: Optional[str]=None
    content: Optional[str]=None
    destination_id: Optional[id]=None
    '''
