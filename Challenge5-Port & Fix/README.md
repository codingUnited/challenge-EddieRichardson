# Port & Fix — Modernized Implementation

## 🚀 Project Overview
This repository contains my modern reimplementation of the **“Port & Fix”** coding challenge.  
The goal: take a buggy, undocumented C++11 console app and **reverse-engineer, debug, and port** it into a clean, maintainable solution in Python (with tests, logging, and error handling).

For the original challenge description and legacy code, see [legacy/README-legacy.md](./legacy/README-legacy.md).

---

## 📂 Repository Structure
.
├── README.md              # This file (solution overview + quickstart)
├── legacy/                # Original buggy C++11 source + challenge docs
│   ├── Buggy.cpp
│   └── README-legacy.md
├── src/                   # Modern implementation (Python package)
│   └── portfix/
│       ├── cli.py
│       ├── core/
│       └── io/
├── tests/                 # Automated test suite
└── docs/                  # (Optional) design notes, architecture decisions

---

## 🛠️ Getting Started

### 1. Clone and checkout branch
git clone <your-repo-url>
cd port-and-fix
git checkout feature/port-and-fix

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the app
python -m portfix.cli --input samples/sample1.txt --output out/result.json --verbose

### 4. Run tests
pytest -q

---

## 🧪 Testing Strategy
- **Golden tests:** lock in behavior from legacy app outputs  
- **Edge cases:** at least 3 discovered during reverse-engineering  
- **Unit tests:** core logic functions  
- **CLI tests:** argument parsing, error handling  

---

## 📖 Notes
- Legacy code is preserved in `legacy/` for reference only.  
- All fixes and design decisions are documented in commit messages and/or `docs/`.  
- Assumptions and deviations from legacy behavior are tracked in `CHANGELOG.md`.  

---

## 📚 References
- [Legacy Challenge Description](./legacy/README-legacy.md)
