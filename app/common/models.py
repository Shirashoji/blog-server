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
    comments = relationship("Comment", back_populates="user")


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
    comments = relationship("Comment", back_populates="blog")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)

    blog_id = Column(Integer, ForeignKey("blogs.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    blog = relationship("Blog", back_populates="comments")
    user = relationship("User", back_populates="comments")
