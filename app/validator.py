def validate_title(title):
    if not title or title.strip() == "":
        raise ValueError("Empty title")