# 🔄 Development Workflow

This file describes how to work locally and keep changes synchronized with GitHub.  
It ensures that code, tests, and documentation evolve together in a clean, traceable way.

---

## 📂 Branching Strategy
- Always create a new branch for each bug fix, feature, or documentation update.
- Branch names should be short and descriptive:
  - `fix-signup-crash`
  - `feature-add-json-persistence`
  - `docs-update-testing-strategy`

---

## 📝 Commit Guidelines
- Make **small, atomic commits** — one logical change per commit.
- Use clear, imperative commit messages:
  - ✅ `Fix signup crash by initializing new User`
  - ✅ `Add regression test for duplicate ISBN`
  - ❌ `misc changes`
- Include related test updates in the same commit.

---

## 🧪 Testing Before Push
- Always run the test suite locally:
  ```bash
  pytest -q
