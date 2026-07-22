# FastAPI application entrypoint.
from fastapi import FastAPI
from app.routers import auth, posts

app = FastAPI(title="test-greenfield", version="0.1.0")

app.include_router(auth.router, prefix="/api/v1")
app.include_router(posts.router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {"status": "ok"}
