# 🏗️ Architecture Blueprint (Updated)

This document describes the modernized architecture for the Port & Fix project.

---

## 🎯 Goals
- Replace raw pointers with safe references (Python objects).  
- Separate concerns: CLI, core logic, IO, persistence.  
- Ensure testability and maintainability.  
- Provide graceful error handling and exit.  

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
    persistence/
      memory.py     # In-memory store
      json_store.py # Optional JSON persistence

---

## 🔄 Data Flow

1. **CLI Layer**  
   - Parse args, configure logging, dispatch commands.  

2. **Core Layer**  
   - `users.py`: login, signup, sessions.  
   - `books.py`: CRUD, ISBN validation.  
   - `engine.py`: reading logic.  

3. **IO Layer**  
   - Input/output formatting.  

4. **Persistence Layer**  
   - In-memory dicts for users/books.  
   - Optional JSON save/load.  

---

## 🧪 Testing Strategy
- Unit tests for core logic.  
- Integration tests for CLI.  
- Golden tests for parity with legacy.  
- Edge case tests for invalid input, empty books, duplicates.  

---

## 📖 Notes
- Architecture avoids manual memory management.  
- Extensible for future web API or GUI.