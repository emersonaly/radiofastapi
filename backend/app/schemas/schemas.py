
from pydantic import BaseModel
from typing import Optional

# --- Token Schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# --- User Schemas ---
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    is_active: bool = True

    class Config:
        orm_mode = True

# --- Station Schemas ---
class StationBase(BaseModel):
    name: str
    stream_url: str
    genre: Optional[str] = ""
    is_active: bool = True

class StationCreate(StationBase):
    pass

class StationOut(StationBase):
    id: int
    
    class Config:
        orm_mode = True
