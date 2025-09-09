from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, database

# Crear tablas
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="RadioFastAPI Backend")

# Dependency
get_db = database.get_db

@app.get("/")
def read_root():
    return {"message": "RadioFastAPI funcionando!"}

# Listar todas las estaciones
@app.get("/stations/", response_model=list[schemas.StationOut])
def list_stations(db: Session = Depends(get_db)):
    return db.query(models.Station).all()

# Crear una estación nueva
@app.post("/stations/", response_model=schemas.StationOut)
def create_station(station: schemas.StationCreate, db: Session = Depends(get_db)):
    db_station = models.Station(**station.dict())
    db.add(db_station)
    db.commit()
    db.refresh(db_station)
    return db_station
