# 🔄 Development Workflow

_Last updated: 2025‑10‑08_

This document describes how to work locally and keep changes synchronized with GitHub.  
It ensures that code, tests, and documentation evolve together in a clean, traceable way.

---

## 📂 Branching Strategy
- Always create a new branch for each bug fix, feature, or documentation update.
- Branch names should be short and descriptive:
  - `fix-signup-crash`
  - `feature-add-json-persistence`
  - `docs-update-testing-strategy`
- Never commit directly to `main`.

---

## 📝 Commit Guidelines
- Make **small, atomic commits** — one logical change per commit.
- Use clear, imperative commit messages:
  - ✅ `Fix signup crash by initializing new User`
  - ✅ `Add regression test for duplicate ISBN`
  - ❌ `misc changes`
- Include related test updates in the same commit.
- Reference issue numbers or doc updates when relevant.

---

## 🧪 Testing Before Push
- Always run the test suite locally:
  pytest --cov=src/portfix
- Ensure all regression, edge case, and integration tests pass before pushing.
- Coverage must remain at **100%** — no regressions allowed.
- Add new tests for every bug fix or feature.

---

## 🚀 Pushing to GitHub
1. Push your branch:
   git push origin fix-signup-crash
2. Open a Pull Request (PR) on GitHub:
   - **Title:** Short summary of the change.
   - **Description:** 
     - Link to the relevant bug/assumption in docs.
     - Explain the fix or feature.
     - Mention new/updated tests.
     - Note any updates to docs (`bugs.md`, `assumptions.md`, etc.).

---

## 🔗 Docs & Code Together
- If you fix a bug → update `docs/bugs.md` with “Fixed in commit <hash>”.
- If you clarify behavior → update `docs/assumptions.md`.
- If you discover a new quirk → update `docs/reverse-engineering.md`.
- Always update `CHANGELOG.md` with a summary of the change.
- Cross‑reference the **Case Study** in the README or `reverse-engineering.md` if the change relates to a legacy bug.
- Keep docs and code in sync in the same PR whenever possible.

---

## ✅ Pre‑Merge Checklist
- [ ] All tests pass (`pytest --cov=src/portfix`)
- [ ] Coverage remains at 100%
- [ ] Docs updated (`bugs.md`, `assumptions.md`, `reverse-engineering.md`, `CHANGELOG.md`)
- [ ] Commit messages are clear and atomic
- [ ] PR description links to relevant docs/bugs
- [ ] Code formatted and linted (`black .` and `ruff check .`)

---

## ✅ Merging
- Merge via PR once tests pass and review is complete.
- Use **squash and merge** to keep history clean.
- Delete the feature branch after merge to keep the repo tidy.

---

## 🔄 Staying Up to Date
- Before starting new work:
  git checkout main
  git pull origin main
  git checkout -b new-feature

---

## 📝 Example Flow
1. Write failing test for bug in `tests/test_users.py`.
2. Commit: `Add regression test for signup crash`.
3. Implement fix in `users.py`.
4. Commit: `Fix signup crash by initializing new User`.
5. Run tests → all pass.
6. Push branch → open PR → merge.
7. Update `docs/bugs.md` and `CHANGELOG.md` with commit reference.

---

## 📖 Notes
- Tests are your safety net — never merge without them.
- Keep PRs small and focused for easier review.
- Treat docs as first-class citizens: update them alongside code.
- Run formatters and linters before pushing to maintain consistency.
- Every change should leave the project in a better state than before.
