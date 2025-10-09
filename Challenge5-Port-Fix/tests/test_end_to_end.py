# tests/test_end_to_end.py

import subprocess
import sys
import textwrap
import pytest

@pytest.mark.integration
def test_full_user_flow(tmp_path):
    """
    End-to-end test: signup → login → add book → read → exit
    """

    # Adjust this command if your CLI entrypoint differs
    cmd = [sys.executable, "-m", "portfix.cli"]

    # Simulated user input sequence (update numbers to match your menu)
    user_input = textwrap.dedent("""\
        1
        testuser
        password123
        2
        testuser
        password123
        3
        12345
        The Hobbit
        J.R.R. Tolkien
        In a hole in the ground there lived a hobbit.
        4
        12345
        5
    """)

    result = subprocess.run(
        cmd,
        input=user_input.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=tmp_path
    )

    # Decode with fallback so invalid bytes don’t crash the test
    stdout = result.stdout.decode("utf-8", errors="replace")
    stderr = result.stderr.decode("utf-8", errors="replace")

    # Ensure CLI exited cleanly
    assert result.returncode == 0, (
    f"CLI crashed!\n\n"
    f"STDOUT:\n{stdout}\n\n"
    f"STDERR:\n{stderr}"
)

    # Check for key flow markers (case-insensitive)
    menu_text = stdout.lower()
    assert "signup" in menu_text
    assert "login" in menu_text
    assert "add book" in menu_text
    assert "read book" in menu_text
    assert "exit" in menu_text

    # Verify book was added and read
    assert "Book added." in stdout
    assert "In a hole in the ground" in stdout
