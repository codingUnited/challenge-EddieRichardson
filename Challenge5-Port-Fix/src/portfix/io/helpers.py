# portfix/io/helpers.py

def safe_input(prompt):
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        return ""
