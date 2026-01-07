from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskModelTest(TestCase):

    def test_task_creation(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")

    def test_default_status_pending(self):
        task = Task.objects.create(title="Another Task")
        self.assertEqual(task.status, "Pending")


class TaskAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_task_returns_201(self):
        response = self.client.post('/api/tasks/', {
            'title': 'New Task'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_tasks_returns_200(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_status_returns_400(self):
        response = self.client.post('/api/tasks/', {
            'title': 'Invalid Task',
            'status': 'Done'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
