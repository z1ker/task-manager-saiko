import unittest
from app.core import add_task, list_tasks
from app.storage import tasks

class TestCore(unittest.TestCase):

    def setUp(self):
        # очищаємо tasks перед кожним тестом
        tasks.clear()

    def test_add_task_success(self):
        task = add_task("My Task")
        self.assertEqual(task["title"], "My Task")
        self.assertFalse(task["done"])
        self.assertIn(task, list_tasks())

    def test_add_task_invalid_title(self):
        import app.core as core
        from app.validator import validate_title

        # Перевірка, що порожній заголовок викликає ValueError
        with self.assertRaises(ValueError):
            add_task("")

        with self.assertRaises(ValueError):
            add_task("   ")

if __name__ == "__main__":
    unittest.main()