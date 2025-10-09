from portfix.core.engine import LibraryEngine
from portfix.io.helpers import safe_input

def main():
    engine = LibraryEngine()
    while True:
        print("\n--- Menu ---")
        print("1. Signup")
        print("2. Login")
        print("3. Add Book")
        print("4. Read Book")
        print("5. Exit")

        choice = safe_input("Choose an option: ")
        if choice == "1":
            u, p = input("Username: "), input("Password: ")
            print(engine.signup(u, p)[1])
        elif choice == "2":
            u, p = input("Username: "), input("Password: ")
            print(engine.login(u, p)[1])
        elif choice == "3":
            isbn = input("ISBN: ")
            title = input("Title: ")
            author = input("Author: ")
            pages = input("Pages (comma separated): ").split(",")
            print(engine.add_book(isbn, title, author, pages)[1])
        elif choice == "4":
            isbn = input("ISBN: ")
            success, msg = engine.read_page(isbn)
            print(msg)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
