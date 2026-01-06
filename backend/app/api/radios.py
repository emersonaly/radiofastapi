
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from backend.app.db import database, models
from backend.app.schemas import schemas
from backend.app.core import config

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login/access-token")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.settings.SECRET_KEY, algorithms=[config.settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
        
    user = db.query(models.User).filter(models.User.username == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user

@router.get("/", response_model=List[schemas.StationOut])
def read_stations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(database.get_db)
):
    """
    Retrieve stations. Public endpoint (requirement was just specific improvements, keeping read public usually makes sense for a radio app, but creating should be protected).
    """
    stations = db.query(models.Station).offset(skip).limit(limit).all()
    return stations

@router.post("/", response_model=schemas.StationOut)
def create_station(
    station: schemas.StationCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Create new station. Protected.
    """
    db_station = models.Station(**station.dict())
    db.add(db_station)
    db.commit()
    db.refresh(db_station)
    return db_station

@router.delete("/{station_id}", response_model=schemas.StationOut)
def delete_station(
    station_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Delete a station. Protected.
    """
    station = db.query(models.Station).filter(models.Station.id == station_id).first()
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    
    db.delete(station)
    db.commit()
    return station
