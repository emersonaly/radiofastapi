
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "RadioFastAPI"
    SECRET_KEY: str = "supersecretkeychangeinproduction"  # Change this!
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str = "sqlite:///./stations.db"

    class Config:
        env_file = ".env"

settings = Settings()
