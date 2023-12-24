from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from src.core.bloom_filter import BloomFilter
from src.db import crud, models, schemas
from src.db.database import SessionLocal, engine
from src.utils.helpers import user_added_response, check_username_response

# API config
app = FastAPI()

origins = ['http://localhost:5000']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_methods=['*'],
                   allow_headers=['*'],
                   )

# Database config
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Bloom filter initialization
crud.filter = BloomFilter(50, 0.05)


# Routes

@app.get('/')
def root():
    return {'status': True, 'message': 'API running...'}


@app.post("/bloom/users/add/")
def add(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_created = crud.create_user(db, user)

    return user_added_response(user_created)

@app.post("/bloom/users/available/")
def check_username(user: schemas.UserBase, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    return check_username_response(db_user)

@app.get("/bloom/users/")
def get_users(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users



