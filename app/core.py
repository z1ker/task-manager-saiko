from app.validator import validate_title
from app.storage import save, get_all

def add_task(title):
    validate_title(title)
    task = {"title": title, "done": False}
    save(task)
    return task

def list_tasks():
    return get_all()