# Server Logs [Iteration 0]

## Platform - OS + python version
- OS: linux
- Python: 3.14.4

## Database
- Original URLs : postgresql+asyncpg://myuser:mypassword@localhost:5432/gen_b65476772e
- Resolved URLs : postgresql+asyncpg://myuser:mypassword@localhost:5432/gen_b65476772e
- Env file      : .env_834719376c65ba67

## Start Script - which script was used
- start.sh (PORT=45023)

## Files Generated / Modified
- /mnt/c/Users/RYZEN/Desktop/projects/fast_api_generator_backend/repos/834719376c65ba67/app/database.py - OK
- /mnt/c/Users/RYZEN/Desktop/projects/fast_api_generator_backend/repos/834719376c65ba67/app/core/security.py - OK
- /mnt/c/Users/RYZEN/Desktop/projects/fast_api_generator_backend/repos/834719376c65ba67/tests/conftest.py - OK
- /mnt/c/Users/RYZEN/Desktop/projects/fast_api_generator_backend/repos/834719376c65ba67/app/main.py - OK
- /mnt/c/Users/RYZEN/Desktop/projects/fast_api_generator_backend/repos/834719376c65ba67/tests/test_stats.py - OK
- /mnt/c/Users/RYZEN/Desktop/projects/fast_api_generator_backend/repos/834719376c65ba67/.env_834719376c65ba67 - OK
- /mnt/c/Users/RYZEN/Desktop/projects/fast_api_generator_backend/repos/834719376c65ba67/start.sh - OK

## API Test Results

| Method | Path | Status | HTTP Code | Notes |
|---|---|---:|---:|---|
| GET | /health | PASSED | 200 | Health check OK |
| GET | /stats | PASSED | 200 | Returns totals and status counts |
| POST | /api/v1/auth/register | PASSED | 201 | User registration |
| POST | /api/v1/auth/login | PASSED | 200 | User login |
| GET | /api/v1/auth/me | PASSED | 200 | Authenticated user info |
| GET | /api/v1/auth/me | PASSED | 401 | Invalid token rejected |
| POST | /api/v1/posts | PASSED | 201 | Create post |
| GET | /api/v1/posts | PASSED | 200 | List posts |
| GET | /api/v1/posts/{post_id} | PASSED | 200 | Get post |
| PUT | /api/v1/posts/{post_id} | PASSED | 200 | Update post |
| DELETE | /api/v1/posts/{post_id} | PASSED | 204 | Delete post |

## Errors Fixed This Iteration
1. start.sh -> hardcoded port 60829 -> use PORT env/default 45023

## Still Failing

