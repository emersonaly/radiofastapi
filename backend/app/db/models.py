
from sqlalchemy import Column, Integer, String, Boolean
from backend.app.db.database import Base

class Station(Base):
    __tablename__ = "stations"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    stream_url = Column(String, nullable=False)
    genre = Column(String, default="")
    is_active = Column(Boolean, default=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
