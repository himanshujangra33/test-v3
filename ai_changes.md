COMMIT_MESSAGE: Add stats endpoint and update env configuration
## Features Added
- Added /stats endpoint returning user/post totals and post status counts.
- Added stats endpoint coverage in tests.

## Files Modified
- app/main.py — added /stats endpoint and database aggregation.
- app/database.py — load env from .env_834719376c65ba67.
- app/core/security.py — load env from .env_834719376c65ba67 and read SECRET_KEY from env.
- tests/conftest.py — load env from .env_834719376c65ba67.
- start.sh — honor PORT env/default 45023.
- server_logs.md — updated iteration 0 results.

## Files Added
- tests/test_stats.py — validates /stats endpoint response.
- .env_834719376c65ba67 — runtime configuration values.

## Secrets Extracted
- SECRET_KEY -> written to .env_834719376c65ba67

## DB URLs Resolved
- postgresql+asyncpg://myuser:mypassword@localhost:5432/gen_b65476772e -> postgresql+asyncpg://myuser:mypassword@localhost:5432/gen_b65476772e

## Test Results Summary
- 10 PASSED, 0 FAILED, 0 SKIPPED
