"""Module for task storage."""

tasks = []

def save(task):
    """Save a task to the storage."""
    tasks.append(task)

def get_all():
    """Return all tasks."""
    return tasks