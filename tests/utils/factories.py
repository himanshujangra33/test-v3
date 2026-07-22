# Factory helpers for test payloads.
from app.models import PostStatus


def user_payload(email: str = "user@example.com", password: str = "Password123"):
    return {"email": email, "password": password}


def login_payload(email: str = "user@example.com", password: str = "Password123"):
    return {"email": email, "password": password}


def post_payload(title: str = "Test Post", content: str = "Test content", status: str = PostStatus.draft):
    status_value = status.value if hasattr(status, "value") else status
    return {"title": title, "content": content, "status": status_value}
