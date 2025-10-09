# 🐞 Bug Fix Journal

_Last updated: 2025‑10‑08_

This file tracks bugs discovered in the legacy app and how they were fixed in the modern implementation.

---

## 🧾 Bug Entries

### Bug #1 — Sign-Up Crash
- **Symptom:** Crash when signing up a new user.  
- **Root Cause:** `current_user` is null in `DoSignUp()`.  
- **Fix:** Initialize a new `User` object before calling `Read()`.  
- **Test:** `tests/test_users.py::test_signup_creates_user`

---

### Bug #2 — Database Reset on Login
- **Symptom:** All sign-ups lost after login.  
- **Root Cause:** `LoadDatabase()` wipes map each login.  
- **Fix:** Separate initialization from login; persist users in memory.  
- **Test:** `tests/test_users.py::test_users_persist_after_login`

---

### Bug #3 — Duplicate ISBNs Allowed
- **Symptom:** Admin can add multiple books with same ISBN.  
- **Root Cause:** `AddBook()` overwrites map entry.  
- **Fix:** Validate ISBN uniqueness before insertion.  
- **Test:** `tests/test_books.py::test_duplicate_isbn_rejected`

---

### Bug #4 — Truncated Input
- **Symptom:** Titles/authors truncated at first space.  
- **Root Cause:** `cin >> str` only reads tokens.  
- **Fix:** Use `getline` (C++) or `input()` (Python).  
- **Test:** `tests/test_books.py::test_full_title_and_author`

---

### Bug #5 — Empty Book Crash
- **Symptom:** Crash when reading empty book.  
- **Root Cause:** Accessing `pages[0]` when vector empty.  
- **Fix:** Validate non-empty pages before adding book.  
- **Test:** `tests/test_books.py::test_empty_book_rejected`

---

### Bug #6 — GetBook Always Null
- **Symptom:** `GetBook()` returns `nullptr`.  
- **Root Cause:** Stub not implemented.  
- **Fix:** Implement lookup by ISBN.  
- **Test:** `tests/test_books.py::test_get_book_by_isbn`

---

### Bug #7 — Infinite Loop
- **Symptom:** Program never exits.  
- **Root Cause:** `Run()` has no exit option.  
- **Fix:** Add “Exit” to main menu.  
- **Test:** `tests/test_system.py::test_exit_option`

---

### Bug #8 — Invalid Input Handling
- **Symptom:** Recursive retry on invalid integer input.  
- **Root Cause:** `ReadInt()` uses recursion for retries.  
- **Fix:** Replace recursion with iterative retry loop.  
- **Test:** `tests/test_cli.py::test_invalid_input_retry`

---

## 📂 How to Use This Journal
- Record each bug with: Symptom → Root Cause → Fix → Test.  
- Keep entries concise but detailed enough for future maintainers.  
- Link to commits or test cases where possible.  
- Update this journal whenever a new bug is discovered or fixed.  
