from __future__ import annotations
from sqlalchemy.orm import Session
from . import models, schemas

filter: "BloomFilter" = None


def create_user(db: Session, user: schemas.UserCreate) -> bool:
    username_taken = get_user_by_username(db, user.username)
    if username_taken:
        return False

    # At this point, we know that the username is not taken, so we're going to add it to the bloom filter
    # and the database!

    filter.add(user.username)

    fake_hashed_password = "fakehashed" + user.password
    user = models.User(username=user.username, password=fake_hashed_password)

    # Adding and committing the user to the database
    db.add(user)
    db.commit()
    db.refresh(user)

    return True


def get_user_by_username(db: Session, username: str):
    # Before we check the database, we use the bloom filter
    username_in_filter = filter.check_existence(username)

    db_user = None
    if username_in_filter:
        # We don't really know if the username is taken, so we're going to check the database
        db_user = db.query(models.User).filter(models.User.username == username).first()
        print('Db checked!')

    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.User).offset(skip).limit(limit).all()
