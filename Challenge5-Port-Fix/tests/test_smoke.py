# tests/test_smoke.py

import pytest
from portfix.core.engine import LibraryEngine

@pytest.mark.smoke
def test_smoke_signup_login_add_read():
    """Critical path: signup -> login -> add book -> read first page"""
    engine = LibraryEngine()
    # Signup
    success, msg = engine.signup("alice", "pw")
    assert success
    # Login
    success, msg = engine.login("alice", "pw")
    assert success
    # Add book
    success, msg = engine.add_book("123", "Title", "Author", ["Page 1", "Page 2"])
    assert success
    # Read page
    success, msg = engine.read_page("123")
    assert success and "Page 1" in msg

@pytest.mark.smoke
def test_smoke_cli_exit(monkeypatch, capsys):
    """Critical path: CLI starts and exits cleanly"""
    inputs = iter(["5"])  # choose Exit immediately
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    from portfix.cli import main
    main()
    captured = capsys.readouterr()
    assert "Goodbye" in captured.out
