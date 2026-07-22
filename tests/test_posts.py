# Tests for post CRUD endpoints.
from uuid import uuid4
import pytest
from tests.utils.factories import login_payload, post_payload, user_payload


def _unique_email(prefix: str = "writer") -> str:
    return f"{prefix}_{uuid4().hex}@example.com"


async def _auth_headers(client, email=None, register_first=True):
    email = email or _unique_email()
    if register_first:
        await client.post("/api/v1/auth/register", json=user_payload(email=email))
    token_response = await client.post("/api/v1/auth/login", json=login_payload(email=email))
    token = token_response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.mark.asyncio
async def test_create_post(client):
    headers = await _auth_headers(client)
    response = await client.post("/api/v1/posts", json=post_payload(), headers=headers)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Post"


@pytest.mark.asyncio
async def test_list_posts(client, seeded_data):
    response = await client.get("/api/v1/posts")
    assert response.status_code == 200
    assert len(response.json()) >= 2


@pytest.mark.asyncio
async def test_get_post(client, seeded_data):
    post_id = str(seeded_data["posts"][0].id)
    response = await client.get(f"/api/v1/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id


@pytest.mark.asyncio
async def test_update_post(client, seeded_data):
    post = seeded_data["posts"][0]
    headers = await _auth_headers(
        client,
        email=seeded_data["users"][0].email,
        register_first=False,
    )
    response = await client.put(
        f"/api/v1/posts/{post.id}",
        json={"title": "Updated"},
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated"


@pytest.mark.asyncio
async def test_delete_post(client, seeded_data):
    post = seeded_data["posts"][1]
    headers = await _auth_headers(
        client,
        email=seeded_data["users"][1].email,
        register_first=False,
    )
    response = await client.delete(f"/api/v1/posts/{post.id}", headers=headers)
    assert response.status_code == 204
