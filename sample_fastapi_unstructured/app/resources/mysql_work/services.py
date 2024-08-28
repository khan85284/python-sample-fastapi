from typing import Annotated, List

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from . import db_models
from .db_engine import SessionLocal, engine
from .models import PostBase, UserBase

db_models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


async def create_post(post: PostBase, db: db_dependency):
    """method to create a post to Database"""
    db_post = db_models.Post(**post.model_dump())
    db.add(db_post)
    db.commit()


async def create_user(user: UserBase, db: db_dependency):
    """method to create a User to Database"""
    db_user = db_models.User(**user.model_dump())
    db.add(db_user)
    db.commit()


async def read_user(user_id: int, db: db_dependency):
    """method to Fetch a user info from a Database"""
    user = db.query(db_models.User).filter(db_models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return user


async def read_post(post_id: int, db: db_dependency):
    """method to Fetch a Post info from a Database"""
    post = db.query(db_models.Post).filter(db_models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return post


async def delete_post(post_id: int, db: db_dependency):
    """method to Delete a post info from a Database"""
    db_post = db.query(db_models.Post).filter(db_models.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(db_post)
    db.commit()


async def read_all_users(db: db_dependency):
    """Fetch all users from the database."""
    users = db.query(db_models.User).all()

    if not users:
        raise HTTPException(status_code=404, detail="No users found")

    return users


async def read_all_posts(db: db_dependency):
    """Fetch all users from the database."""
    posts = db.query(db_models.Post).all()

    if not posts:
        raise HTTPException(status_code=404, detail="No users found")

    return posts
