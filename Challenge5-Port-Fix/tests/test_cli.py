# tests/test_cli.py

import sys
import pytest
import runpy
from portfix.cli import main

@pytest.mark.cli
def test_invalid_input_retry(monkeypatch, capsys):
    # Simulate invalid choice then exit
    inputs = iter(["99", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("portfix.io.helpers.safe_input", lambda prompt: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Invalid option" in captured.out
    assert "Goodbye" in captured.out

def test_cli_entrypoint(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")
    sys.modules.pop("portfix.cli", None)  # remove cached module
    runpy.run_module("portfix.cli", run_name="__main__")
