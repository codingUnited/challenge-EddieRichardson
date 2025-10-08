# 🔍 Reverse-Engineering Ledger

_Last updated: 2025‑10‑08_  
_Source: Buggy.cpp (commit <hash>)_

This document captures observed behaviors of the legacy C++11 app.  
It serves as a reference for parity testing, bug discovery, and clarifying intended behavior.

---

## 📂 How to Use This Ledger
- **Input / Action**: The command-line invocation or user action performed.  
- **Legacy Output / Behavior**: What the buggy C++11 app actually did.  
- **Intended Behavior**: What the modern implementation should do.  
- **Notes**: Any quirks, crashes, or assumptions made.  
- **Test**: The regression or parity test that covers this case.  

Update this table as you test more cases. Each row should eventually link to a corresponding test.

---

## 🧾 Ledger Table

| Input / Action            | Legacy Output / Behavior            | Intended Behavior                  | Notes                                             | Test |
|----------------------------|-------------------------------------|------------------------------------|--------------------------------------------------|------|
| Sign Up (new user)         | Crash (null `current_user`)         | Create new user and store in map    | `DoSignUp()` uses `current_user` before init      | `tests/test_users.py::test_signup_creates_user` |
| Login after Sign Up        | Sign-ups lost                       | Persist users across session        | `LoadDatabase()` wipes map each login             | `tests/test_users.py::test_users_persist_after_login` |
| Add Book (Admin) — ISBN    | Accepts duplicate ISBNs             | Reject duplicates with error        | No validation in `BooksManager::AddBook`          | `tests/test_books.py::test_duplicate_isbn_rejected` |
| Add Book (Admin) — Strings | Title/author truncated at first space | Accept full strings               | `cin >> str` only reads tokens                    | `tests/test_books.py::test_full_title_and_author` |
| Read Book with 0 pages     | Crash on access                     | Reject empty books or handle safely | `GetPages()[current_page]` out of range           | `tests/test_books.py::test_empty_book_rejected` |
| BooksManager::GetBook      | Always returns `nullptr`            | Return book by ISBN                 | Stub not implemented                              | `tests/test_books.py::test_get_book_by_isbn` |
| OnlineReaderSystem::Run    | Infinite loop, no exit              | Provide exit option                 | Only “Login/Sign Up” loop                         | `tests/test_system.py::test_exit_option` |
| ReadInt() invalid input    | Recursive retry                     | Iterative retry                     | Risk of stack overflow                            | `tests/test_cli.py::test_invalid_input_retry` |

---

## 🧪 Edge Cases to Explore
- Empty input file or empty book (0 pages).  
- Multi-word titles/authors (currently truncated).  
- Duplicate ISBNs when adding books.  
- Invalid login credentials (wrong username/password).  
- Sign-up with username already taken.  
- Reading history when no sessions exist.  
- Navigating past first/last page of a book.  
- Very large number of pages (stress test).  
- Invalid menu input (non-integer, out of range).  
- Exiting the system gracefully (currently impossible).  

---

## 📖 Notes
- Many issues stem from raw pointers and manual memory management.  
- Input handling is fragile (no spaces, no validation).  
- Persistence is absent — every run resets users and books.
