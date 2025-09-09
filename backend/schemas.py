from pydantic import BaseModel

class StationBase(BaseModel):
    name: str
    stream_url: str
    genre: str = ""
    is_active: bool = True

class StationCreate(StationBase):
    pass

class StationOut(StationBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2
