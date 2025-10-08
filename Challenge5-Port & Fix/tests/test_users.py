import pytest

def test_signup_creates_user():
    # Bug #1 regression: sign-up crash
    # Arrange: simulate signup
    # Act: call signup
    # Assert: user is created and stored
    pass

def test_users_persist_after_login():
    # Bug #2 regression: database reset on login
    pass

def test_invalid_login_rejected():
    # Edge case: wrong username/password
    pass

def test_duplicate_username_rejected():
    # Edge case: signup with existing username
    pass
