"""Module for validating task input."""

def validate_title(title):
    """Check if the title is a non-empty string. Raise ValueError if invalid."""
    if not isinstance(title, str) or title.strip() == "":
        raise ValueError("Invalid title")