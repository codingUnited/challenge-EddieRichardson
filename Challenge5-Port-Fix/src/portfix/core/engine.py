from .users import User
from .books import Book

class LibraryEngine:
    def __init__(self):
        self.users = {}
        self.books = {}
        self.current_user = None

    # User management
    def signup(self, username, password):
        if username in self.users:
            return False, "User already exists."
        self.users[username] = User(username, password)
        return True, "Signup successful."

    def login(self, username, password):
        user = self.users.get(username)
        if not user or user.password != password:
            return False, "Invalid credentials."
        self.current_user = user
        return True, f"Welcome {username}!"

    # Book management
    def add_book(self, isbn, title, author, pages):
        if isbn in self.books:
            return False, "Book already exists."
        self.books[isbn] = Book(isbn, title, author, pages)
        return True, "Book added."

    def get_book(self, isbn):
        return self.books.get(isbn)

    # Reading system
    def read_page(self, isbn):
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
