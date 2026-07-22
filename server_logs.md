# Server Logs [Iteration 0]

## Platform — OS + python version
- OS: linux
- Python: 3.14.4

## Database
- Client URL  : postgresql+asyncpg://myuser:mypassword@localhost:5432/gen_b65476772e
- Fallback    : YES — substituted (original unreachable). DB name: gen_b65476772e. Log in server_logs.md.
- Resolved URL: postgresql+asyncpg://myuser:mypassword@localhost:5432/gen_b65476772e

## Test Runner — no live server needed
- pytest tests/ -v --tb=short  (tests use ASGI transport / TestClient — no HTTP server required)

## Files Generated / Modified
- /app/__init__.py — OK
- /app/database.py — OK
- /app/models.py — OK
- /app/schemas.py — OK
- /app/core/__init__.py — OK
- /app/core/security.py — OK
- /app/core/auth.py — OK
- /app/routers/__init__.py — OK
- /app/routers/auth.py — OK
- /app/routers/posts.py — OK
- /app/main.py — OK
- /seed.py — OK
- /requirements.txt — OK
- /.env_4cb7114e-dc00-4a30-bd4f-f3fb96d29919 — OK
- /start.sh — OK
- /start.bat — OK
- /Dockerfile — OK
- /docker-compose.yml — OK
- /Makefile — OK
- /README.md — OK
- /pytest.ini — OK
- /tests/__init__.py — OK
- /tests/conftest.py — OK
- /tests/test_auth.py — OK
- /tests/test_posts.py — OK
- /tests/utils/__init__.py — OK
- /tests/utils/factories.py — OK

## API Test Results

| Test Function | Endpoint | Status | Expected Code | Notes |
|---|---|---:|---:|---|
| health_check | GET /health | PASSED | 200 | curl http://localhost:60829/health |
| test_register | POST /api/v1/auth/register | PASSED | 201 | User registered |
| test_login_valid | POST /api/v1/auth/login | PASSED | 200 | Token issued |
| test_me | GET /api/v1/auth/me | PASSED | 200 | Current user |
| test_invalid_token | GET /api/v1/auth/me | PASSED | 401 | Invalid token |
| test_create_post | POST /api/v1/posts | PASSED | 201 | Post created |
| test_list_posts | GET /api/v1/posts | PASSED | 200 | Posts list |
| test_get_post | GET /api/v1/posts/{post_id} | PASSED | 200 | Post fetched |
| test_update_post | PUT /api/v1/posts/{post_id} | PASSED | 200 | Post updated |
| test_delete_post | DELETE /api/v1/posts/{post_id} | PASSED | 204 | Post deleted |

## Errors Fixed This Iteration
1. /app/schemas.py → response validation errors → switched id fields to UUID and fixed schema corruption.
2. /tests/conftest.py → event loop mismatch + duplicate seeds → added session loop scope and seeded users/posts deterministically.
3. /tests/test_posts.py → ownership mismatch → ensured posts belong to seeded users.

