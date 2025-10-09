# core/books.py

class Book:
    def __init__(self, isbn: str, title: str, author: str, pages: list[str]):
        # Validate required fields
        if not isbn:
            raise ValueError("ISBN cannot be empty")
        if not title or not author:
            raise ValueError("Book must have a title and an author")
        if not pages or len(pages) == 0:
            raise ValueError("Book must have at least one page")

        # Core attributes
        self.isbn = isbn
        self.title = title.strip()
        self.author = author.strip()
        self.pages = pages
        # Track current page for this book (per user progress is tracked in User)
        self.current_page = 0

    def __str__(self) -> str:
        """User-friendly string, good for CLI output."""
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

    def __repr__(self) -> str:
        """Developer-friendly representation, useful in debugging."""
        return (
            f"Book(isbn={self.isbn!r}, title={self.title!r}, "
            f"author={self.author!r}, pages={len(self.pages)})"
        )

    def __len__(self) -> int:
        """Number of pages in the book."""
        return len(self.pages)

    def turn_page(self, direction: int = 1) -> str:
        """
        Move forward/backward one page safely.
        Returns the text of the new current page.
        """
        new_page = self.current_page + direction
        if 0 <= new_page < len(self.pages):
            self.current_page = new_page
        return self.pages[self.current_page]

    def get_page(self, page: int) -> str:
        """Jump to a specific page. Raises IndexError if out of range."""
        if page < 0 or page >= len(self.pages):
            raise IndexError("Page out of range")
        self.current_page = page
        return self.pages[page]


class BookDB:
    """In‑memory book database. Responsible for adding, retrieving, and listing books."""

    def __init__(self):
        # Dictionary of isbn -> Book object
        self._books: dict[str, Book] = {}

    def add_book(self, isbn: str, title: str, author: str, pages: list[str]) -> Book:
        """Add a new book. Rejects duplicate ISBNs and invalid data."""
        if isbn in self._books:
            raise ValueError(f"Duplicate ISBN '{isbn}' not allowed")
        book = Book(isbn, title, author, pages)
        self._books[isbn] = book
        return book

    def get_book(self, isbn: str) -> Book | None:
        """Retrieve a book by ISBN, or None if not found."""
        return self._books.get(isbn)

    def all_books(self) -> list[Book]:
        """Return a list of all books in the database."""
        return list(self._books.values())