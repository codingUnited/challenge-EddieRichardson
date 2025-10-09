# 🏗️ Architecture Blueprint (Updated)

_Last updated: 2025‑10‑08_

This document describes the modernized architecture for the Port & Fix project.

---

## 🎯 Goals
- Replace raw pointers with safe references (Python objects).  
- Separate concerns: CLI, core logic, IO, persistence.  
- Ensure testability and maintainability.  
- Provide graceful error handling and exit.  
- Keep modules small, composable, and easy to extend.  

---

## 📂 Module Layout

src/
  portfix/
    cli.py          # CLI entry point
    core/
      users.py      # User and session management
      books.py      # Book management (CRUD, validation)
      engine.py     # Core reading logic
    io/
      parser.py     # Input parsing (if needed)
      writer.py     # Output formatting
    util/
      log.py        # Logging setup
      errors.py     # Custom exceptions and error handling
    persistence/
      memory.py     # In-memory store
      json_store.py # Optional JSON persistence
    adapters/
      legacy.py     # (Optional) Legacy compatibility or migration helpers

---

## 🔄 Data Flow

1. **CLI Layer**  
   - Parse args, configure logging, dispatch commands.  
   - Provide entry point for user interaction.  

2. **Core Layer**  
   - `users.py`: login, signup, sessions, reading history.  
   - `books.py`: CRUD, ISBN validation, duplicate rejection.  
   - `engine.py`: reading logic, page navigation, session state.  

3. **IO Layer**  
   - Input parsing and output formatting.  
   - Decouples user-facing strings from core logic.  

4. **Persistence Layer**  
   - In-memory dicts for users/books (default).  
   - Optional JSON save/load for persistence across runs.  

5. **Utility Layer**  
   - Logging, error handling, reusable helpers.  
   - Keeps cross-cutting concerns isolated.  

---

## 🧪 Testing Strategy
- **Unit tests** for each core module (`users`, `books`, `engine`).  
- **Integration tests** for CLI flows (signup, login, add book, read book).  
- **Golden tests** for parity with legacy outputs.  
- **Edge case tests** for invalid input, empty books, duplicates, exit behavior.  
- **Regression tests** for every bug fixed (linked to Bug Fix Journal).  

---

## 📖 Notes
- Architecture avoids manual memory management and recursion pitfalls.  
- Designed for clarity and onboarding: each module has a single responsibility.  
- Extensible for future adapters (e.g., web API, GUI, or database backend).  
- Documentation (ledger, bug journal, assumptions) stays in sync with code.  
