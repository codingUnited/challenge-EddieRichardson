# core/engine.py

from .users import User
from .books import Book

class LibraryEngine:
    """
    High‑level orchestrator for the library system.
    Manages users, books, and reading sessions.
    """

    def __init__(self):
        # In‑memory stores for users and books
        self.users: dict[str, User] = {}
        self.books: dict[str, Book] = {}
        # Tracks the currently logged‑in user
        self.current_user: User | None = None

    # ---------------- User Management ----------------
    def signup(self, username: str, password: str):
        """Register a new user. Returns (success, message)."""
        if username in self.users:
            return False, "User already exists."
        self.users[username] = User(username, password)
        return True, "Signup successful."

    def login(self, username: str, password: str):
        """Authenticate a user and set as current. Returns (success, message)."""
        user = self.users.get(username)
        if not user or user.password != password:
            return False, "Invalid credentials."
        self.current_user = user
        return True, f"Welcome {username}!"

    # ---------------- Book Management ----------------
    def add_book(self, isbn: str, title: str, author: str, pages: list[str]):
        """Add a new book. Returns (success, message)."""
        if isbn in self.books:
            return False, "Book already exists."
        if not title or not author:
            return False, "Title and author required."
        if not pages or len(pages) == 0:
            return False, "Book must have at least one page."
        self.books[isbn] = Book(isbn, title, author, pages)
        return True, "Book added."

    def get_book(self, isbn: str) -> Book | None:
        """Retrieve a book by ISBN, or None if not found."""
        return self.books.get(isbn)

    # ---------------- Reading System ----------------
    def read_page(self, isbn: str):
        """
        Read the next page of a book for the current user.
        Advances the user's page counter and returns (success, message).
        """
        if not self.current_user:
            return False, "No user logged in."
        book = self.get_book(isbn)
        if not book:
            return False, "Book not found."
        page_num = self.current_user.current_page.get(isbn, 0)
        if page_num >= len(book.pages):
            return False, "End of book."
        page_text = book.pages[page_num]
        self.current_user.current_page[isbn] = page_num + 1
        return True, f"Page {page_num+1}: {page_text}"