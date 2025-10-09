# tests/test_users.py

import pytest
from portfix.core.users import UserDB, User

@pytest.mark.users
def test_signup_creates_user():
    db = UserDB()
    user = db.add_user("alice", "pw")
    assert user.username == "alice"
    assert db.get_user("alice") is user

@pytest.mark.users
def test_users_persist_after_login():
    db = UserDB()
    db.add_user("bob", "pw")
    user = db.authenticate("bob", "pw")
    assert user.username == "bob"
    # Persistence: user still exists after login
    assert db.get_user("bob") is user

@pytest.mark.users
def test_duplicate_username_rejected():
    db = UserDB()
    db.add_user("charlie", "pw")
    with pytest.raises(ValueError):
        db.add_user("charlie", "pw2")

@pytest.mark.users
def test_invalid_login_rejected():
    db = UserDB()
    db.add_user("dave", "pw")
    with pytest.raises(ValueError):
        db.authenticate("dave", "wrongpw")
    with pytest.raises(ValueError):
        db.authenticate("not_a_user", "pw")

@pytest.mark.users
def test_login_with_wrong_password(userdb):
    userdb.add_user("alice", "pw")
    with pytest.raises(ValueError):
        userdb.authenticate("alice", "wrong")

@pytest.mark.users
def test_login_with_unknown_user(userdb):
    with pytest.raises(ValueError):
        userdb.authenticate("ghost", "pw")

@pytest.mark.users
def test_all_users_returns_list():
    db = UserDB()
    db.add_user("eve", "pw")
    db.add_user("frank", "pw")
    users = db.all_users()
    assert isinstance(users, list)
    assert {u.username for u in users} == {"eve", "frank"}

@pytest.mark.users
def test_user_set_and_get_page():
    user = User("alice", "pw")
    # Initially no progress
    assert user.get_page("123") is None
    # After setting progress
    user.set_page("123", 5)
    assert user.get_page("123") == 5