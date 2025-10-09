# tests/test_helpers.py

import pytest
from portfix.io import helpers

@pytest.mark.helpers
def test_safe_input_strips_whitespace(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "   hello   ")
    result = helpers.safe_input("Enter something: ")
    assert result == "hello"

@pytest.mark.helpers
def test_safe_input_returns_empty_on_eof(monkeypatch):
    # Simulate EOFError
    monkeypatch.setattr("builtins.input", lambda _: (_ for _ in ()).throw(EOFError))
    result = helpers.safe_input("Enter something: ")
    assert result == ""

@pytest.mark.helpers
def test_safe_input_returns_empty_on_keyboard_interrupt(monkeypatch):
    # Simulate Ctrl-C
    monkeypatch.setattr("builtins.input", lambda _: (_ for _ in ()).throw(KeyboardInterrupt))
    result = helpers.safe_input("Enter something: ")
    assert result == ""
