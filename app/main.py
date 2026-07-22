# FastAPI application entrypoint.
from fastapi import Depends, FastAPI
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Post, User
from app.routers import auth, posts

app = FastAPI(title="test-greenfield", version="0.1.0")

app.include_router(auth.router, prefix="/api/v1")
app.include_router(posts.router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/stats")
async def stats(db: AsyncSession = Depends(get_db)):
    users_count = await db.scalar(select(func.count()).select_from(User))
    posts_count = await db.scalar(select(func.count()).select_from(Post))
    status_rows = await db.execute(
        select(Post.status, func.count(Post.id)).group_by(Post.status)
    )
    posts_by_status = {
        (status.value if hasattr(status, "value") else str(status)): count
        for status, count in status_rows.all()
    }
    return {
        "users": users_count or 0,
        "posts": posts_count or 0,
        "posts_by_status": posts_by_status,
    }


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.get("/ding")
async def ding():
    return {"message": "dong"}
