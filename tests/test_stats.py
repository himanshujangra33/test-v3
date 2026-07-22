from dotenv import load_dotenv

load_dotenv('.env_834719376c65ba67', override=True)

import pytest


@pytest.mark.asyncio
async def test_stats_endpoint(client, seeded_data):
    response = await client.get("/stats")
    assert response.status_code == 200
    data = response.json()
    assert data["users"] >= 2
    assert data["posts"] >= 2
    assert "posts_by_status" in data
