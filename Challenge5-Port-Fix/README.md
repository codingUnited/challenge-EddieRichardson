# 📚 Port & Fix — Modernized Implementation

_Last updated: 2025‑10‑08_

## 🚀 Project Overview
This repository contains my modern reimplementation of the **“Port & Fix”** coding challenge.  
The challenge: take a buggy, undocumented C++11 console app (`Buggy.cpp`) and **reverse‑engineer, debug, and port** it into a clean, maintainable Python solution.

The result is a **menu‑driven CLI application** with:
- Modular design (`User`, `Book`, `LibraryEngine`, helpers)
- Full pytest suite with **100% coverage**
- Documentation of every bug in the legacy code and how it was fixed
- A case study narrative showing the transformation from C++ to Python

For the original challenge description and legacy code, see [legacy/README-legacy.md](./legacy/README-legacy.md).

---

## 📂 Repository Structure
.
├── README.md              # Project overview + quickstart  
├── legacy/                # Original buggy C++11 source + challenge docs  
│   ├── Buggy.cpp  
│   └── README-legacy.md  
├── src/                   # Modern implementation (Python package)  
│   └── portfix/  
│       ├── cli.py         # CLI entry point  
│       ├── core/          # Core logic (users, books, engine)  
│       ├── io/            # Input/output helpers  
│       └── util/          # Utilities  
├── tests/                 # pytest suite (unit, integration, regression)  
│   ├── conftest.py        # Shared fixtures  
│   ├── test_users.py  
│   ├── test_books.py  
│   ├── test_engine.py  
│   ├── test_cli.py  
│   └── test_system.py  
├── docs/                  # Engineering docs  
│   ├── reverse-engineering.md  
│   ├── bugs.md  
│   ├── assumptions.md  
│   ├── architecture.md  
│   ├── testing.md
│   ├── index.md   
│   └── future.md  
├── WORKFLOW.md            # Contributor workflow guide  
└── CHANGELOG.md           # Chronological project log  

---

## 🛠️ Getting Started

### 1. Clone and checkout branch
git clone <your-repo-url>  
cd Challenge5-Port-Fix  
git checkout feature/port-and-fix  

### 2. Install dependencies
pip install -r requirements.txt  

### 3. Run the app
python -m portfix.cli  

You’ll see an interactive menu:

--- Menu ---  
1. Signup  
2. Login  
3. Add Book  
4. Read Book  
5. Exit  

### 4. Run tests
pytest --cov=src/portfix  

---

## 🧪 Testing Strategy
- **Unit tests:** core logic functions (`users.py`, `books.py`, `engine.py`)  
- **Integration tests:** CLI flows (signup → login → add book → read book)  
- **Regression tests:** one per bug identified in `docs/bugs.md`  
- **Edge cases:** from `docs/reverse-engineering.md` and `docs/testing.md`  
- **Coverage:** currently **100% across all modules**

---

## 📖 Case Study: From Buggy.cpp to Python
The original `Buggy.cpp` was a teaching tool: it simulated an online reader system but was riddled with flaws:

- Raw pointers and manual memory management  
- Broken signup logic (undefined behavior)  
- Lost data on every login (dummy database reload)  
- Incomplete methods (`GetBook` always returned `nullptr`)  
- Brittle input handling (`cin >>` everywhere)  
- No persistence, no tests  

The Python port (`portfix`) fixes every major flaw:

- Safe, modular classes (`User`, `Book`, `LibraryEngine`)  
- Clean CLI with robust input handling  
- User progress tracked per book without dangling pointers  
- Memory safety via Python’s garbage collection  
- Full pytest suite with 100% coverage  
- Documentation of every bug and its fix  

See [docs/reverse-engineering.md](./docs/reverse-engineering.md) for the full before/after analysis.

---

## 🔄 Workflow
- Follow `WORKFLOW.md` for branching, commits, and PRs.  
- Update `docs/bugs.md` and `docs/assumptions.md` as you discover quirks.  
- Keep docs and code in sync in the same PR.  
- Summarize fixes and features in `CHANGELOG.md`.  

---

## 📚 References
- [Legacy Challenge Description](./legacy/README-legacy.md)  
- [Reverse Engineering Case Study](./docs/reverse-engineering.md)  
- [Bug Ledger](./docs/bugs.md)  
- [Architecture](./docs/architecture.md)  
- [Assumptions](./docs/assumptions.md)  
- [Testing](./docs/testing.md)  
- [Index](./docs/index.md)  
- [Future Work](./docs/future.md)  

---
