from django.test import TestCase
from tasks.models import Task

class TaskModelTest(TestCase):

    def test_task_creation(self):
        """Task can be created with a title"""
        task = Task.objects.create(title="Learn Django REST")
        self.assertEqual(task.title, "Learn Django REST")
        # Default status should be Pending
        self.assertEqual(task.status, "Pending")
