# tests/test_engine.py

import pytest
from portfix.core.engine import LibraryEngine

@pytest.mark.engine
def test_read_page_advances():
    engine = LibraryEngine()
    engine.signup("alice", "pw")
    engine.login("alice", "pw")
    engine.add_book("123", "Title", "Author", ["Page 1", "Page 2"])
    success, msg = engine.read_page("123")
    assert success and "Page 1" in msg
    success, msg = engine.read_page("123")
    assert success and "Page 2" in msg

@pytest.mark.engine
def test_read_page_end_of_book():
    engine = LibraryEngine()
    engine.signup("bob", "pw")
    engine.login("bob", "pw")
    engine.add_book("456", "Title", "Author", ["Only Page"])
    engine.read_page("456")  # consume page
    success, msg = engine.read_page("456")
    assert not success and "End of book" in msg

@pytest.mark.engine
def test_read_page_requires_login():
    engine = LibraryEngine()
    engine.add_book("789", "Title", "Author", ["Page 1"])
    success, msg = engine.read_page("789")
    assert not success and "No user logged in" in msg

@pytest.mark.engine
def test_read_nonexistent_book(engine):
    engine.signup("alice", "pw")
    engine.login("alice", "pw")
    success, msg = engine.read_page("not-there")
    assert not success
    assert "not found" in msg.lower()

@pytest.mark.engine
def test_read_requires_login(engine):
    engine.add_book("123", "Title", "Author", ["Page 1"])
    success, msg = engine.read_page("123")
    assert not success
    assert "No user logged in" in msg

@pytest.mark.engine
def test_read_nonexistent_book(engine):
    engine.signup("alice", "pw")
    engine.login("alice", "pw")
    success, msg = engine.read_page("not-there")
    assert not success
    assert "not found" in msg.lower()

@pytest.mark.engine
def test_signup_duplicate_user():
    engine = LibraryEngine()
    success, msg = engine.signup("alice", "pw")
    assert success
    # Try again with same username
    success, msg = engine.signup("alice", "pw")
    assert not success
    assert "already exists" in msg

@pytest.mark.engine
def test_login_invalid_credentials():
    engine = LibraryEngine()
    engine.signup("bob", "pw")
    # Wrong password
    success, msg = engine.login("bob", "wrong")
    assert not success
    assert "invalid" in msg.lower()
    # Nonexistent user
    success, msg = engine.login("ghost", "pw")
    assert not success

@pytest.mark.engine
def test_add_book_duplicate_and_invalid():
    engine = LibraryEngine()
    # Valid add
    success, msg = engine.add_book("123", "Title", "Author", ["Page 1"])
    assert success
    # Duplicate ISBN
    success, msg = engine.add_book("123", "Other", "Author", ["Page 1"])
    assert not success
    # Missing title
    success, msg = engine.add_book("456", "", "Author", ["Page 1"])
    assert not success
    # Missing author
    success, msg = engine.add_book("789", "Title", "", ["Page 1"])
    assert not success
    # Empty pages
    success, msg = engine.add_book("999", "Title", "Author", [])
    assert not success