from sqlalchemy import create_engine
from sqalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./db.sqlite3"

DB_ENGINE = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=DB_ENGINE)
