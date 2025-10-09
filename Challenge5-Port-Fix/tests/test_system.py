# tests/test_system.py

import pytest
from portfix.core.engine import LibraryEngine

@pytest.mark.system
def test_exit_option(monkeypatch, capsys):
    # Simulate choosing exit immediately
    inputs = iter(["5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    from portfix.cli import main
    main()
    captured = capsys.readouterr()
    assert "Goodbye" in captured.out

@pytest.mark.system
def test_full_flow_signup_login_add_read_exit(monkeypatch, capsys):
    # Simulate a full flow: signup -> login -> add book -> read -> exit
    inputs = iter([
        "1", "alice", "pw",     # signup
        "2", "alice", "pw",     # login
        "3", "123", "Title", "Author", "Page1,Page2",  # add book
        "4", "123",             # read page
        "5"                     # exit
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    from portfix.cli import main
    main()
    captured = capsys.readouterr()
    assert "Signup successful" in captured.out
    assert "Welcome alice" in captured.out
    assert "Book added" in captured.out
    assert "Page 1" in captured.out
    assert "Goodbye" in captured.out
