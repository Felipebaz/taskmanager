import unittest
from task_manager import Task, TaskManager
import os

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Use a test file to avoid overwriting real data
        self.test_filename = "test_tasks.json"
        TaskManager.FILENAME = self.test_filename
        self.manager = TaskManager()
        self.manager.tasks = []
        self.manager.next_id = 1
        self.manager.save_tasks()

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_add_task(self):
        self.manager.add_task("Test task")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].description, "Test task")
        self.assertFalse(self.manager.tasks[0].completed)

    def test_complete_task(self):
        self.manager.add_task("Test task")
        self.manager.complete_task(1)
        self.assertTrue(self.manager.tasks[0].completed)

    def test_delete_task(self):
        self.manager.add_task("Test task")
        self.manager.delete_task(1)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_list_tasks_empty(self):
        self.manager.tasks = []
        # Should print 'No tasks found.'
        self.manager.list_tasks()

    def test_list_tasks_non_empty(self):
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        self.manager.list_tasks()

if __name__ == "__main__":
    unittest.main()
