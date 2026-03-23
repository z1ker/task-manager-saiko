import unittest
from app.core import add_task, list_tasks
from app.storage import tasks

class TestCore(unittest.TestCase):
    """Unit tests for core.py functions."""

    def setUp(self):
        """Очистити tasks перед кожним тестом."""
        tasks.clear()

    def test_add_task_success(self):
        """Перевірка успішного додавання завдання."""
        task = add_task("My Task")
        self.assertEqual(task["title"], "My Task")
        self.assertFalse(task["done"])
        self.assertIn(task, list_tasks())

    def test_add_task_invalid_title(self):
        """Перевірка, що некоректний заголовок викликає ValueError."""
        with self.assertRaises(ValueError):
            add_task("")

        with self.assertRaises(ValueError):
            add_task("   ")

if __name__ == "__main__":
    # Щоб тести точно запускалися при запуску файлу
    import sys
    import os
    # Додаємо корінь проєкту в PYTHONPATH для правильного імпорту
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    unittest.main()