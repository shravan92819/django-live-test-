from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class TaskAPITest(APITestCase):

    def setUp(self):
        self.list_create_url = reverse("task-list")  # Make sure your urls.py has name='task-list'

    def test_create_task_returns_201(self):
        """POST /api/tasks/ should create a task"""
        data = {"title": "API Test Task"}
        response = self.client.post(self.list_create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "API Test Task")
        self.assertEqual(response.data["status"], "Pending")  # default status

    def test_list_tasks_returns_200(self):
        """GET /api/tasks/ should return 200"""
        # Create a task first
        self.client.post(self.list_create_url, {"title": "List Test Task"}, format="json")
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_invalid_status_returns_400(self):
        """Creating task with invalid status should return 400"""
        data = {"title": "Invalid Status", "status": "Pendinsg"}  # typo
        response = self.client.post(self.list_create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("status", response.data)
