from pydantic import BaseModel
from typing import List, Optional

class Config:
    from_attributes = True 

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
  class Config:
    orm_mode = True 

class User(BaseModel):
  name: str
  email: str
  password: str

class ShowUser(BaseModel):
  name: str
  email: str
  blogs: List[Blog] = []
  password: str
  
  class Config:
        orm_mode = True

class ShowBlog(Blog): #response mode 
    title: str
    body: str
    creator: ShowUser
    
    class Config:
        orm_mode = True

class login(BaseModel):
  email: str
  password: str

class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  email: Optional[str] = None

