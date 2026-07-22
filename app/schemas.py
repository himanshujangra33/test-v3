# Pydantic schemas for API payloads.
from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr
from app.models import PostStatus


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    user_id: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    email: EmailStr
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None


class PostBase(BaseModel):
    title: str
    content: str
    status: PostStatus = PostStatus.draft


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    status: Optional[PostStatus] = None


class PostRead(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    author_id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None
