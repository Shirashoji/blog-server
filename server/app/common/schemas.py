from datetime import datetime
from pydantic import BaseModel


class CommentBase(BaseModel):
    pass


class CommentCreate(CommentBase):
    content: str


class Comment(CommentBase):
    id: int
    content: str
    blog_id: int
    user_id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True


class CommentSummary(CommentBase):
    id: int
    user_id: int
    content: str
    updated_at: datetime | None = None

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class BlogCategoryBase(BaseModel):
    pass


class BlogCategory(BlogCategoryBase):
    blog_id: int
    category_id: int

    class Config:
        orm_mode = True


class BlogBase(BaseModel):
    title: str
    description: str | None = None


class BlogCreate(BlogBase):
    content: str | None = None
    pass


class Blog(BlogBase):
    id: int
    owner_id: int
    content: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    categories: list[Category] = []
    comments: list[CommentSummary] = []

    class Config:
        orm_mode = True


class BlogSummary(BlogBase):
    id: int
    updated_at: datetime | None = None

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    username: str
    joined_at: datetime | None = None
    blogs: list[BlogSummary] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
