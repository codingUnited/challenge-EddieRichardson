# 📜 Changelog

_Last updated: 2025‑10‑08_

All notable changes to this project will be documented in this file.  
This format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]
- Placeholder for upcoming fixes and features.

---

## [0.2.0] - 2025-10-08
### Added
- Full end-to-end CLI integration test (`test_full_user_flow`) covering signup → login → add book → read → exit.
- `pytest.ini` with custom markers (`users`, `books`, `engine`, `helpers`, `cli`, `system`, `smoke`, `integration`) and default coverage options.
- `test_cli_entrypoint` to exercise the `__main__` guard, ensuring complete coverage of `cli.py`.

### Changed
- CLI input handling aligned with test harness (page entry sequence clarified).
- Updated `WORKFLOW.md` to include coverage reporting, linting, and pre-merge checklist.
- Refined test assertions to match actual CLI output (e.g., `Signup` vs. `Sign Up`).

### Fixed
- Resolved `EOFError` in CLI integration tests by correcting input sequence.
- Eliminated `PytestUnknownMarkWarning` by registering custom markers.
- Achieved 100% test coverage across all modules, including `cli.py`.

### Notes
- **Phase 1 milestone complete**: stable port, documented architecture, and fully tested baseline.

---

## [0.1.0] - 2025-10-08
### Added
- Initial documentation set: `reverse-engineering.md`, `bugs.md`, `assumptions.md`, `architecture.md`, `testing.md`, `index.md`, `future.md`, and `WORKFLOW.md`.
- Test scaffolding with pytest stubs and fixtures.
- Root-level `README.md` with project overview.

### Fixed
- Documented legacy bugs and quirks from `Buggy.cpp`.

### Notes
- This is the first tracked version of the port-and-fix project.

---

## 🛣 Roadmap
- **Phase 2**: Extend functionality (e.g., richer book management, improved CLI UX, persistent storage).
- **Phase 3**: Advanced features (multi-user sessions, search, analytics, export/import).
- **Ongoing**: Maintain 100% coverage, refine documentation, and streamline contributor onboarding.
