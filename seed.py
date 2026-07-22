# Seed script to populate the database with sample data.
import asyncio
from dotenv import load_dotenv
from sqlalchemy import select
from app.database import Base, AsyncSessionLocal, engine
from app.models import Post, PostStatus, User
from app.core.security import get_password_hash

load_dotenv('.env_4cb7114e-dc00-4a30-bd4f-f3fb96d29919', override=True)


async def seed_data():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as session:
        existing_users = (await session.execute(select(User))).scalars().all()
        if existing_users:
            return

        users = [
            User(email="alice@example.com", hashed_password=get_password_hash("Password123")),
            User(email="bob@example.com", hashed_password=get_password_hash("Password123")),
            User(email="carol@example.com", hashed_password=get_password_hash("Password123")),
        ]
        session.add_all(users)
        await session.flush()

        posts = [
            Post(
                title="Welcome to the Blog",
                content="First post content",
                status=PostStatus.published,
                author_id=users[0].id,
            ),
            Post(
                title="Draft Thoughts",
                content="Work in progress",
                status=PostStatus.draft,
                author_id=users[1].id,
            ),
            Post(
                title="Another Update",
                content="More content here",
                status=PostStatus.published,
                author_id=users[2].id,
            ),
        ]
        session.add_all(posts)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(seed_data())
