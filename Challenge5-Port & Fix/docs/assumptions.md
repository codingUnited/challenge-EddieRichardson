# 🤔 Assumptions & Decisions

_Last updated: 2025‑10‑08_

This file records assumptions made while porting the legacy app.

---

## 🧾 Assumption Log

### Assumption #1 — Persistence
- **Observation:** Legacy resets users/books each run.  
- **Decision:** Modern version will persist state in memory for session; optional JSON persistence later.  
- **Test:** `tests/test_system.py::test_users_persist_in_memory`

---

### Assumption #2 — ISBN Uniqueness
- **Observation:** Legacy allows duplicates.  
- **Decision:** ISBNs must be unique; duplicates rejected.  
- **Test:** `tests/test_books.py::test_duplicate_isbn_rejected`

---

### Assumption #3 — Input Strings
- **Observation:** Legacy truncates at spaces.  
- **Decision:** Accept full strings for titles/authors/pages.  
- **Test:** `tests/test_books.py::test_full_title_and_author`

---

### Assumption #4 — Empty Books
- **Observation:** Legacy allows empty books → crash.  
- **Decision:** Reject empty books at creation.  
- **Test:** `tests/test_books.py::test_empty_book_rejected`

---

### Assumption #5 — Exit Behavior
- **Observation:** Legacy runs forever.  
- **Decision:** Provide explicit “Exit” option in main menu.  
- **Test:** `tests/test_system.py::test_exit_option`

---

### Assumption #6 — Error Handling
- **Observation:** Legacy uses recursion for invalid input.  
- **Decision:** Use iterative retry with clear error messages.  
- **Test:** `tests/test_cli.py::test_invalid_input_retry`

---

## 📖 Notes
- Each assumption should be traceable to a test or commit.  
- Superseded assumptions should remain documented for historical context.  
- Update this file as new ambiguities arise during development.
