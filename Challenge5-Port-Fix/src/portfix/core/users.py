# core/users.py

class User:
    def __init__(self, username, password):
        # Unique identifier for the user
        self.username = username
        # Plaintext password for now (could be hashed in future extension)
        self.password = password
        # Tracks reading progress: {isbn -> current page number}
        self.current_page = {}

    def set_page(self, isbn: str, page: int):
        """Update the current page number for a given book."""
        self.current_page[isbn] = page

    def get_page(self, isbn: str) -> int | None:
        """Retrieve the last page number read for a given book, or None if not started."""
        return self.current_page.get(isbn)


class UserDB:
    """In‑memory user database. Responsible for sign‑up, login, and persistence during runtime."""

    def __init__(self):
        # Dictionary of username -> User object
        self._users: dict[str, User] = {}

    def add_user(self, username: str, password: str) -> User:
        """Create a new user. Rejects duplicate usernames."""
        if username in self._users:
            raise ValueError(f"Username '{username}' already exists")
        user = User(username, password)
        self._users[username] = user
        return user

    def authenticate(self, username: str, password: str) -> User:
        """Validate credentials. Raises ValueError if invalid."""
        user = self._users.get(username)
        if not user or user.password != password:
            raise ValueError("Invalid username or password")
        return user

    def get_user(self, username: str) -> User | None:
        """Fetch a user by username, or None if not found."""
        return self._users.get(username)

    def all_users(self) -> list[User]:
        """Return a list of all registered users."""
        return list(self._users.values())
