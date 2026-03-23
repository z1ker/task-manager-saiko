"""Core functions for task management."""

from app.validator import validate_title
from app.storage import save, get_all

def add_task(title):
    """Add a new task with the given title."""
    validate_title(title)
    print("Start adding task")
    task = {"title": title2, "done": False}
    save(task)
    print("Task added:", title)
    return task

def list_tasks():
    """Return all saved tasks."""
    return get_all()
