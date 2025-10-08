# tests/conftest.py
import pytest

from portfix.core.users import UsersManager, User
from portfix.core.books import BooksManager, Book

@pytest.fixture
def sample_user():
    """Return a sample non-admin user."""
    user = User()
    user.set_username("alice")
    user.set_password("secret")
    user.set_email("alice@example.com")
    user.set_name("Alice Example")
    return user

@pytest.fixture
def sample_admin():
    """Return a sample admin user."""
    admin = User()
    admin.set_username("admin")
    admin.set_password("adminpass")
    admin.set_email("admin@example.com")
    admin.set_name("Admin User")
    admin.set_is_library_admin(True)
    return admin

@pytest.fixture
def sample_book():
    """Return a sample book with multiple pages."""
    book = Book()
    book.set_isbn("12345")
    book.set_author("Test Author")
    book.set_title("Test Driven Development in Action")
    book.set_pages(["Page 1", "Page 2", "Page 3"])
    return book

@pytest.fixture
def users_manager(sample_user, sample_admin):
    """UsersManager preloaded with one user and one admin."""
    mgr = UsersManager()
    mgr.add_user(sample_user)
    mgr.add_user(sample_admin)
    return mgr

@pytest.fixture
def books_manager(sample_book):
    """BooksManager preloaded with one book."""
    mgr = BooksManager()
    mgr.add_book(sample_book)
    return mgr
