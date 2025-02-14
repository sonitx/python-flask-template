from app.models.user_model import User

def get_users():
    return [
        {"id": 1, "username": "john_doe", "email": "john@example.com"},
        {"id": 2, "username": "jane_doe", "email": "jane@example.com"}
    ]
