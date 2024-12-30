from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from django.urls import reverse


class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            completed=False,
            user=self.user
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.user.username, 'testuser')
        self.assertFalse(self.task.completed)

class TaskViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            completed=False,
            user=self.user
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('tasks:task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')

    def test_task_create_view(self):
        response = self.client.post(reverse('tasks:task_create'), {
            'title': 'New Task',
            'description': 'New Description',
            'completed': False,
        })
        self.assertEqual(response.status_code, 302)  # Redirige después de crear
        self.assertEqual(Task.objects.last().title, 'New Task')