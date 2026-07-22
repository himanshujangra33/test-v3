# Tests for authentication endpoints.
from uuid import uuid4
import pytest
from tests.utils.factories import login_payload, user_payload


def _unique_email(prefix: str = "user") -> str:
    return f"{prefix}_{uuid4().hex}@example.com"


@pytest.mark.asyncio
async def test_register(client):
    email = _unique_email("register")
    response = await client.post("/api/v1/auth/register", json=user_payload(email=email))
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == email


@pytest.mark.asyncio
async def test_login_valid(client):
    email = _unique_email("login")
    await client.post("/api/v1/auth/register", json=user_payload(email=email))
    response = await client.post("/api/v1/auth/login", json=login_payload(email=email))
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


@pytest.mark.asyncio
async def test_me(client):
    email = _unique_email("me")
    await client.post("/api/v1/auth/register", json=user_payload(email=email))
    token_response = await client.post("/api/v1/auth/login", json=login_payload(email=email))
    token = token_response.json()["access_token"]
    response = await client.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["email"] == email


@pytest.mark.asyncio
async def test_invalid_token(client):
    response = await client.get(
        "/api/v1/auth/me", headers={"Authorization": "Bearer invalidtoken"}
    )
    assert response.status_code == 401
