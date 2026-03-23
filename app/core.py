from app.validator import validate_title

tasks = []

def add_task(title):
    validate_title(title)
    task = {"title": title, "done": False}
    tasks.append(task)
    return task