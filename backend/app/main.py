
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.db.database import engine, Base
from backend.app.api import auth, radios
from backend.app.core.config import settings

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://192.168.0.200:5173",  # External access
    "http://192.168.0.200:8080",  # If using standard serve
    "*"  # Ideally restrict this in prod, but for local dev * is easier
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(radios.router, prefix="/stations", tags=["stations"])

@app.get("/")
def read_root():
    return {"message": "RadioFastAPI Backend V2 is running!"}
