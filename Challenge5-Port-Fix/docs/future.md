# 🚀 Future Roadmap

_Last updated: 2025‑10‑08_

This document outlines the intended direction of the modern Python port.  
It distinguishes between the **parity baseline** (what must be preserved from the legacy app) and **future enhancements** (what we plan to add beyond parity).

---

## ✅ Parity Baseline
The first milestone of this project is to achieve full parity with the legacy C++11 app.  
That means the Python port must support the same core features:  
- User sign‑up/login  
- Adding and retrieving books  
- Reading page by page  
- Navigating via a CLI menu  
- Maintaining state in memory for the session  
- Handling invalid input gracefully  

Only once this baseline is stable will new features be layered on.

---

## 🚀 Future Enhancements
These improvements go beyond parity and represent the next stage of development:

- **Persistence**: JSON or SQLite backend, configurable persistence layer.  
- **User Roles**: Admin vs. regular users, permissions system.  
- **Search & Filtering**: Search by title/author/keyword, filter by ISBN prefix.  
- **Enhanced CLI UX**: Multi‑word input, `--help`/`--verbose`, clearer errors.  
- **Testing & CI**: Golden tests, GitHub Actions pipeline.  
- **Advanced Features**: Reading history, bookmarks, stress‑test handling.  
- **Future Platforms**: Web API (FastAPI), GUI or web frontend.  
- **Performance & Scaling**: Optimize for large datasets, async I/O for web API.  
- **Developer Experience**: Pre‑commit hooks, linting/formatting automation, contributor onboarding docs.  

---

## 🗂️ Roadmap Progress

- [*] **Phase 1 — Core Parity**  
  (Sign‑up/login, add/retrieve books, read pages, CLI menu, in‑memory persistence, error handling)

- [ ] **Phase 2 — Persistence & Roles**  
  (JSON/SQLite persistence, configurable layer, admin vs. regular users)

- [ ] **Phase 3 — UX & Search**  
  (Multi‑word input, clearer prompts, `--help`/`--verbose`, search/filter)

- [ ] **Phase 4 — Testing & CI**  
  (Golden tests, regression tests, GitHub Actions CI)

- [ ] **Phase 5 — Advanced Features**  
  (Reading history, bookmarks, stress‑test handling)

- [ ] **Phase 6 — Platform Expansion**  
  (Web API layer, GUI/web frontend)

- [ ] **Phase 7 — Performance & DX**  
  (Scaling for large datasets, async I/O, developer tooling improvements)

---

## 📖 Notes
- Feature parity must be achieved before enhancements are added.  
- Each enhancement should be logged in `CHANGELOG.md` when implemented.  
- This roadmap is iterative — update as new ideas or requirements emerge.  
- Phases may overlap if enhancements do not compromise parity stability.  
