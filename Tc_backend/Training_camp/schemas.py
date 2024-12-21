from pydantic import BaseModel, Emailstr, Field
from datetime import datetime
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select


class UserBase(SQLModel):
    email:Emailstr
    password:str
    image:bytes
    first_name:str
    last_name:str
    contact:str
    role:enumerate

class User(UserBase, table = True):
    id:int
    password:str


class UserCreate(UserBase):
    password:str

class UserUpdate(UserBase):
    email:Emailstr | None
    password:str   |None
    image:bytes |None
    first_name:str  |None
    last_name:str   |None
    contact:str |None
    role:enumerate  |None

class UserOut(UserBase):
    pass


    

    