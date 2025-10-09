# tests/conftest.py

import pytest
from portfix.core.engine import LibraryEngine
from portfix.core.users import UserDB
from portfix.core.books import BookDB

@pytest.fixture
def engine():
    """Fresh LibraryEngine for each test."""
    return LibraryEngine()

@pytest.fixture
def userdb():
    """Standalone UserDB for unit tests."""
    return UserDB()

@pytest.fixture
def bookdb():
    """Standalone BookDB for unit tests."""
    return BookDB()

@pytest.fixture
def sample_book(bookdb):
    """A sample book preloaded into BookDB."""
    return bookdb.add_book("123", "Sample Title", "Sample Author", ["Page 1", "Page 2"])

@pytest.fixture
def sample_user(userdb):
    """A sample user preloaded into UserDB."""
    return userdb.add_user("alice", "pw")
