from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    joined_at = Column(DateTime, nullable=False)

    blogs = relationship("Blog", back_populates="owner")


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    content = Column(String, index=True)

    owner_id = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    owner = relationship("User", back_populates="blogs")


class Comments(Base):
    __tablename__ = "comments"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    blog_id = Column(Integer, ForeignKey("blogs.id"), primary_key=True)
    content = Column(String, index=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="comments")
    blog = relationship("Blog", back_populates="comments")


class Favorite(Base):
    __tablename__ = "favorites"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    blog_id = Column(Integer, ForeignKey("blogs.id"), primary_key=True)
    timestamp = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="favorites")
    blog = relationship("Blog", back_populates="favorites")