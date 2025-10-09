# 🔄 Development Workflow

_Last updated: 2025‑10‑08_

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
  ```
- Ensure all regression and edge case tests pass before pushing.

---

## 🚀 Pushing to GitHub
1. Push your branch:
   ```bash
   git push origin fix-signup-crash
   ```
2. Open a Pull Request (PR) on GitHub:
   - **Title:** Short summary of the change.
   - **Description:** 
     - Link to the relevant bug/assumption in docs.
     - Explain the fix or feature.
     - Mention new/updated tests.

---

## 🔗 Docs & Code Together
- If you fix a bug → update `bugs.md` with “Fixed in commit <hash>`.
- If you clarify behavior → update `assumptions.md`.
- If you discover a new quirk → update `reverse-engineering.md`.
- Keep docs and code in sync in the same PR when possible.

---

## ✅ Merging
- Merge via PR once tests pass and review is complete.
- Delete the feature branch after merge to keep the repo clean.

---

## 🔄 Staying Up to Date
- Before starting new work:
  ```bash
  git checkout main
  git pull origin main
  git checkout -b new-feature
  ```

---

## 📝 Example Flow
1. Write failing test for bug in `tests/test_users.py`.
2. Commit: `Add regression test for signup crash`.
3. Implement fix in `users.py`.
4. Commit: `Fix signup crash by initializing new User`.
5. Run tests → all pass.
6. Push branch → open PR → merge.
7. Update `bugs.md` with commit reference.

---

## 📖 Notes
- Tests are your safety net — never merge without them.
- Keep PRs small and focused for easier review.
- Treat docs as first-class citizens: update them alongside code.
