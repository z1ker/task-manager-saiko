"""Main program loop for task management."""

from app.core import add_task, list_tasks

def run():
    """Run the main input loop for the program."""
    while True:
        cmd = input("Enter command: ")

        if cmd == "add":
            title = input("Task: ")
            add_task(title)

        elif cmd == "list":
            print(list_tasks())

        elif cmd == "exit":
            break

if __name__ == "__main__":
    run()
    print("Program was started")