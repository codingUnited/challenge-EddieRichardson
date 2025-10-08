# 🧪 Testing Strategy (Updated)

This file outlines the testing approach for the modern implementation.

---

## 🎯 Goals
- Ensure correctness and robustness.  
- Lock in intended behavior vs. legacy quirks.  
- Prevent regressions.  

---

## 📂 Test Types

### Golden Tests
- Compare outputs against legacy where valid.  
- Example: reading book pages, login success.  

### Unit Tests
- `users.py`: signup, login, sessions.  
- `books.py`: add, get, reject duplicates.  
- `engine.py`: page navigation.  

### Integration Tests
- CLI commands: login, signup, add book, read book.  
- End-to-end flows.  

### Edge Case Tests
- Empty book → rejected.  
- Duplicate ISBN → rejected.  
- Invalid login → error.  
- Multi-word titles/authors → accepted.  
- Exit option → terminates gracefully.  

### Regression Tests
- Each bug fixed has a corresponding test.  

---

## 🛠️ Tools
- pytest  
- coverage.py  

---

## 📖 Notes
- Tests run with `pytest -q`.  
- Each new feature/bug fix must include a test.  