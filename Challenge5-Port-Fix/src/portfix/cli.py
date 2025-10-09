#cli.py

from portfix.core.engine import LibraryEngine
from portfix.io.helpers import safe_input

def main():
    """
    Command‑line interface for the library system.
    Provides a simple menu loop for user interaction.
    """
    engine = LibraryEngine()
    while True:
        print("\n--- Menu ---")
        print("1. Signup")
        print("2. Login")
        print("3. Add Book")
        print("4. Read Book")
        print("5. Exit")

        choice = safe_input("Choose an option: ").strip()
        if choice == "1":
            # Sign up a new user
            u, p = input("Username: ").strip(), input("Password: ").strip()
            success, msg = engine.signup(u, p)
            print(msg)
        elif choice == "2":
            # Log in as an existing user
            u, p = input("Username: ").strip(), input("Password: ").strip()
            success, msg = engine.login(u, p)
            print(msg)
        elif choice == "3":
            # Add a new book to the library
            isbn = input("ISBN: ").strip()
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            raw_pages = input("Pages (comma separated): ")
            pages = [p.strip() for p in raw_pages.split(",") if p.strip()]
            success, msg = engine.add_book(isbn, title, author, pages)
            print(msg)
        elif choice == "4":
            # Read the next page of a book
            isbn = input("ISBN: ").strip()
            success, msg = engine.read_page(isbn)
            print(msg)
        elif choice == "5":
            # Exit the system gracefully
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1–5.")

if __name__ == "__main__":
    main()
