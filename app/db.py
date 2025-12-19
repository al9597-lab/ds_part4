from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import PG_HOST, PG_PORT, PG_USER, PG_PASSWORD, PG_DB

DATABASE_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    return SessionLocal()
