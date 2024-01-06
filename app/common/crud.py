import datetime
from sqlalchemy.orm import Session
from common.security import get_password_hash

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed = get_password_hash(user.password)
    db_user = models.User(
        username=user.username, hashed_password=hashed)
    db_user.joined_at = datetime.datetime.now()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_blogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Blog).offset(skip).limit(limit).all()


def get_blog_by_id(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()


def create_blog(db: Session, owner_id: int, blog: schemas.BlogCreate):
    db_blog = models.Blog(**blog.dict(), owner_id=owner_id)
    db_blog.created_at = datetime.datetime.now()
    db_blog.updated_at = datetime.datetime.now()
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def update_blog(db: Session, blog_id: int, blog: schemas.BlogCreate):
    db_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    db_blog.title = blog.title
    db_blog.description = blog.description
    db_blog.content = blog.content
    db_blog.updated_at = datetime.datetime.now()
    db.commit()
    db.refresh(db_blog)
    return db_blog


def delete_blog(db: Session, blog_id: int):
    db_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    db.delete(db_blog)
    db.commit()
    return db_blog


def get_comments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Comment).offset(skip).limit(limit).all()


def get_comment_by_id(db: Session, comment_id: int):
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()


def get_comments_by_blog_id(db: Session, blog_id: int):
    return db.query(models.Comment).filter(models.Comment.blog_id == blog_id).all()


def create_comment(db: Session, blog_id: int, user_id: int, comment: schemas.CommentCreate):
    db_comment = models.Comment(
        **comment.dict(), blog_id=blog_id, user_id=user_id)
    db_comment.created_at = datetime.datetime.now()
    db_comment.updated_at = datetime.datetime.now()
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def update_comment(db: Session, comment_id: int, comment: schemas.CommentCreate):
    db_comment = db.query(models.Comment).filter(
        models.Comment.id == comment_id).first()
    db_comment.content = comment.content
    db_comment.updated_at = datetime.datetime.now()
    db.commit()
    db.refresh(db_comment)
    return db_comment


def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(models.Comment).filter(
        models.Comment.id == comment_id).first()
    db.delete(db_comment)
    db.commit()
    return db_comment
