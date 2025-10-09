# 📚 Documentation Index

_Last updated: 2025‑10‑08_

Welcome to the documentation for the **Port & Fix** project.  
This folder captures the design process, reverse-engineering notes, and technical decisions made while modernizing the legacy C++11 app.

---

## 📂 Contents

- [Architecture & Design](./architecture.md)  
  High-level overview of the new system structure, module boundaries, and rationale for design choices.

- [Reverse-Engineering Ledger](./reverse-engineering.md)  
  Input/output mappings from the legacy app, observed quirks, and intended behavior.

- [Bug Fix Journal](./bugs.md)  
  A running log of discovered bugs, their root causes, fixes, and associated tests.

- [Testing Strategy](./testing.md)  
  Outline of golden tests, edge cases, coverage goals, and any advanced testing approaches.

- [Assumptions & Decisions](./assumptions.md)  
  Documentation of unclear areas in the legacy spec and the decisions made to resolve them.

- [Future Enhancements](./future.md)  
  Ideas for extending the app beyond feature parity (e.g., new outputs, web adapter).

- [Index](./index.md)  
  This file — a map of the documentation set for quick navigation.

---

## 🧭 Usage

Each file in this folder is meant to be **living documentation**:
- Update as you discover new bugs, assumptions, or design insights.  
- Keep entries concise but clear — think of it as a logbook for future maintainers.  
- Cross-link between docs where helpful (e.g., a bug entry linking to the test that covers it).  
- Ensure references stay up to date when files are renamed or reorganized.  
