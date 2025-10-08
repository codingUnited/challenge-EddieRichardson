# 🔍 Reverse-Engineering Ledger

This document captures observed behaviors of the legacy C++11 app.  
It serves as a reference for parity testing, bug discovery, and clarifying intended behavior.

---

## 📂 How to Use This Ledger
- **Input / Action**: The command-line invocation or user action performed.  
- **Legacy Output / Behavior**: What the buggy C++11 app actually did.  
- **Intended Behavior**: What the modern implementation should do.  
- **Notes**: Any quirks, crashes, or assumptions made.  

Update this table as you test more cases. Each row should eventually link to a corresponding test.

---

## 🧾 Ledger Table

| Input / Action | Legacy Output / Behavior | Intended Behavior | Notes |
|----------------|--------------------------|------------------|-------|
| Sign Up (new user) | Crash (null `current_user`) | Create new user and store in map | `DoSignUp()` uses `current_user` before initialization |
| Login after Sign Up | Sign-ups lost | Persist users across session | `LoadDatabase()` wipes map each login |
| Add Book (Admin) | Accepts duplicate ISBNs | Reject duplicates with error | No validation in `BooksManager::AddBook` |
| Add Book (Admin) | Title/author truncated at first space | Accept full strings | `cin >> str` only reads tokens |
| Read Book with 0 pages | Crash on access | Reject empty books or handle gracefully | `GetPages()[current_page]` out of range |
| BooksManager::GetBook | Always returns `nullptr` | Return book by ISBN | Stub not implemented |
| OnlineReaderSystem::Run | Infinite loop, no exit | Provide exit option | Only “Login/Sign Up” loop |
| ReadInt() invalid input | Recursive retry | Iterative retry | Risk of stack overflow |

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
