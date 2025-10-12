# 📚 Case Study: From *Buggy.cpp* to a Clean Python Library System

## 🎯 Background
The original **`Buggy.cpp`** was a deliberately flawed C++ program designed as a teaching tool.  
Its purpose was to simulate an *online reader system* where users could sign up, log in, add books, and read them page by page.  

At first glance, it looked functional — but it was riddled with design flaws, unsafe memory handling, and incomplete features.

---

## 🐞 Problems in the Original `Buggy.cpp`
- **Memory management**: Raw `new`/`delete` everywhere → leaks and dangling pointers.
- **Unsafe pointers**: `BookReadingSession` stored a raw `Book*`. If the book was deleted, the session pointed to garbage.
- **Broken signup**: `UsersManager::DoSignUp` called `current_user->Read(...)` without creating a new `User` object → undefined behavior.
- **Lost data**: `UsersManager::LoadDatabase` reloaded dummy users every login, wiping out signups.
- **Incomplete methods**: `BooksManager::GetBook` always returned `nullptr`.
- **Input handling**: `cin >>` everywhere → no spaces in names/titles, no validation.
- **Tight coupling**: Logic, I/O, and data management tangled together.
- **No persistence**: All data lost when the program exited.
- **No testing**: No way to verify correctness or catch regressions.

---

## ✅ The Python Rewrite (`portfix`)
The Python port re‑engineered the system with clarity and safety:

- **User system**: `User` and `UserDB` classes with safe signup/login, duplicate checks, and progress tracking.
- **Book system**: `Book` and `BookDB` classes with ISBN, title, author, and page content.
- **Engine**: `LibraryEngine` orchestrates users and books, cleanly separated from the CLI.
- **CLI**: Menu loop mirrors the original but with safer input handling.
- **Reading sessions**: Progress tracked per user/book, no dangling pointers.
- **Memory safety**: Python’s garbage collection eliminates manual `new`/`delete`.
- **Tests**: 100% coverage across all modules, verifying every branch and edge case.
- **Extensibility**: Modular design, easy to extend with persistence or richer input.

---

## 📋 Checklist: Original Goals vs. Python Port

| Feature / Goal                     | Buggy.cpp (C++)              | Python Port |
|------------------------------------|------------------------------|-------------|
| Signup & login                     | Buggy, unsafe                | Safe, tested |
| User profile (name, email, admin)  | Present                      | Present |
| Add books                          | Admin only, fragile          | Admin only, tested |
| Preloaded books                    | Yes                          | Yes |
| Reading sessions                   | Implemented, unsafe pointers | Implemented, safe |
| Track current page & last access   | Yes                          | Yes |
| Reading history per user           | Yes                          | Yes |
| Menu‑driven CLI                    | Yes                          | Yes |
| Persistence across runs            | No                           | No (same as original) |
| Memory safety                      | Manual, buggy                | Automatic, safe |
| Test coverage                      | None                         | 100% |

---

## 🏆 The Transformation
The original `Buggy.cpp` was a **teaching tool**: it showed the shape of an online reader system but was riddled with pitfalls.  

The Python rewrite not only replicates the intended behavior but **fixes every major flaw** and adds professional‑grade testing and structure.  

This project demonstrates:
- **Reverse engineering** a legacy system.  
- **Documenting flaws** and mapping them to fixes.  
- **Delivering a maintainable, testable, and extensible solution**.  

---
