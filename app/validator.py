def validate_title(title):
    if not isinstance(title, str) or title.strip() == "":
        raise ValueError("Invalid title")