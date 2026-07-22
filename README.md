# test-greenfield

Blog API built with FastAPI and PostgreSQL.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Environment

Configure `.env_4cb7114e-dc00-4a30-bd4f-f3fb96d29919`:

- `DATABASE_URL` (default: postgresql+asyncpg://myuser:mypassword@localhost:5432/gen_b65476772e)
- `SECRET_KEY`
- `ACCESS_TOKEN_EXPIRE_MINUTES`
- `PORT=60829`

## Run

```bash
bash ./start.sh
```

## API Endpoints

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `GET /api/v1/auth/me`
- `POST /api/v1/posts`
- `GET /api/v1/posts`
- `GET /api/v1/posts/{post_id}`
- `PUT /api/v1/posts/{post_id}`
- `DELETE /api/v1/posts/{post_id}`
- `GET /health`

## Tests

```bash
pytest tests/ -v --tb=short
```

## Docker

```bash
docker compose up --build
```

## Project Tree

```
app/
  core/
  routers/
  database.py
  main.py
  models.py
  schemas.py
seed.py
requirements.txt
start.sh
start.bat
Dockerfile
docker-compose.yml
Makefile
```
