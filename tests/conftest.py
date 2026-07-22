# Pytest fixtures for async database and client setup.
import os
import pytest
from dotenv import load_dotenv
from httpx import ASGITransport, AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

load_dotenv('.env_4cb7114e-dc00-4a30-bd4f-f3fb96d29919', override=True)

from app.main import app
from app.database import Base, get_db
from app.models import Post, PostStatus, User
from app.core.security import get_password_hash

MAIN_DB_URL = os.getenv("DATABASE_URL", "")
_parts = MAIN_DB_URL.rsplit("/", 1)
TEST_DB_URL = (_parts[0] + "/" + _parts[1] + "_test") if len(_parts) == 2 else MAIN_DB_URL


@pytest.fixture(scope="session")
async def db_engine():
    from sqlalchemy.pool import NullPool

    main_engine = create_async_engine(MAIN_DB_URL, poolclass=NullPool)
    async with main_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await main_engine.dispose()

    engine = create_async_engine(TEST_DB_URL, poolclass=NullPool)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()


@pytest.fixture
async def db_session(db_engine):
    factory = async_sessionmaker(db_engine, class_=AsyncSession, expire_on_commit=False)
    async with factory() as session:
        yield session
        await session.rollback()


@pytest.fixture
async def client(db_session):
    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture
async def seeded_data(db_session):
    result = await db_session.execute(
        select(User).where(User.email.in_(["seed1@example.com", "seed2@example.com"]))
    )
    existing_users = {user.email: user for user in result.scalars().all()}

    user1 = existing_users.get("seed1@example.com")
    if user1 is None:
        user1 = User(email="seed1@example.com", hashed_password=get_password_hash("Password123"))
    user2 = existing_users.get("seed2@example.com")
    if user2 is None:
        user2 = User(email="seed2@example.com", hashed_password=get_password_hash("Password123"))

    db_session.add_all([user1, user2])
    await db_session.flush()

    result = await db_session.execute(select(Post).where(Post.author_id == user1.id))
    post1 = result.scalars().first()
    if post1 is None:
        post1 = Post(
            title="Seed Post 1",
            content="Seed content 1",
            status=PostStatus.published,
            author_id=user1.id,
        )
        db_session.add(post1)

    result = await db_session.execute(select(Post).where(Post.author_id == user2.id))
    post2 = result.scalars().first()
    if post2 is None:
        post2 = Post(
            title="Seed Post 2",
            content="Seed content 2",
            status=PostStatus.draft,
            author_id=user2.id,
        )
        db_session.add(post2)

    await db_session.commit()

    return {"users": [user1, user2], "posts": [post1, post2]}
