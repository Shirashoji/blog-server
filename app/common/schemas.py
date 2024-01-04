from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    description: str | None = None
    content: str | None = None


class BlogCreate(BlogBase):
    pass


class Blog(BlogBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    username: str
    blogs: list[Blog] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
