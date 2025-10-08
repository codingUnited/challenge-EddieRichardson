# 📚 Port & Fix — Modernized Implementation

_Last updated: 2025‑10‑08_  
_Source: Buggy.cpp (commit <hash>)_

## 🚀 Project Overview
This repository contains my modern reimplementation of the **“Port & Fix”** coding challenge.  
The goal: take a buggy, undocumented C++11 console app and **reverse-engineer, debug, and port** it into a clean, maintainable Python solution with tests, logging, and error handling.

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
│       └── util/          # Logging, utilities  
├── tests/                 # pytest suite (unit, integration, regression)  
│   ├── conftest.py        # Shared fixtures  
│   ├── test_users.py  
│   ├── test_books.py  
│   ├── test_engine.py  
│   ├── test_cli.py  
│   └── test_system.py  
├── docs/                  # Engineering docs  
│   ├── reverse-engineering.md  
│   ├── index.md  
│   ├── bugs.md  
│   ├── assumptions.md  
│   ├── architecture.md  
│   ├── testing.md  
│   └── future.md  
├── WORKFLOW.md            # Contributor workflow guide  
└── CHANGELOG.md           # Chronological project 

---

## 🛠️ Getting Started

### 1. Clone and checkout branch
```bash
git clone <your-repo-url>
cd port-and-fix
git checkout feature/port-and-fix
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python -m portfix.cli --input samples/sample1.txt --output out/result.json --verbose
```

### 4. Run tests
```bash
pytest -q
```

---

## 🧪 Testing Strategy
- **Golden tests:** lock in behavior from legacy app outputs  
- **Regression tests:** one per bug in `bugs.md`  
- **Edge cases:** from `reverse-engineering.md` and `testing.md`  
- **Unit tests:** core logic functions (`users.py`, `books.py`, `engine.py`)  
- **Integration tests:** CLI flows, login → add book → read book  

---

## 🔄 Workflow
- Follow `WORKFLOW.md` for branching, commits, and PRs.  
- Update `bugs.md` and `assumptions.md` as you discover quirks.  
- Keep docs and code in sync in the same PR.  
- Summarize fixes and features in `CHANGELOG.md`.  

---

## 📖 Notes
- Legacy code is preserved in `legacy/` for reference only.  
- All fixes and design decisions are documented in commits and `/docs/`.  
- Assumptions and deviations from legacy behavior are tracked in `assumptions.md` and `CHANGELOG.md`.  

---

## 📚 References
- [Legacy Challenge Description](./legacy/README-legacy.md)
