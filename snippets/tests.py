from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Snippet, Tag
from django.contrib.auth.models import User

class SnippetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.snippet_data = {'title': 'Test Snippet', 'note': 'This is a test snippet.'}
        self.snippet = Snippet.objects.create(title='Test Snippet', note='This is a test snippet.', created_by=self.user)

    def test_create_snippet(self):
        response = self.client.post(reverse('snippet-list'), self.snippet_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Snippet.objects.count(), 2)

    def test_get_snippet(self):
        response = self.client.get(reverse('snippet-detail', kwargs={'pk': self.snippet.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Snippet')

    def test_update_snippet(self):
        updated_data = {'title': 'Updated Snippet', 'note': 'This is an updated snippet.'}
        response = self.client.put(reverse('snippet-detail', kwargs={'pk': self.snippet.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.snippet.refresh_from_db()
        self.assertEqual(self.snippet.title, 'Updated Snippet')

    def test_delete_snippet(self):
        response = self.client.delete(reverse('snippet-detail', kwargs={'pk': self.snippet.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Snippet.objects.count(), 0)

class TagTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tag_data = {'title': 'Test Tag'}
        self.tag = Tag.objects.create(title='Test Tag')

    def test_create_tag(self):
        response = self.client.post(reverse('tag-list'), self.tag_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 2)

    def test_get_tag(self):
        response = self.client.get(reverse('tag-detail', kwargs={'pk': self.tag.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Tag')

    def test_update_tag(self):
        updated_data = {'title': 'Updated Tag'}
        response = self.client.put(reverse('tag-detail', kwargs={'pk': self.tag.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.title, 'Updated Tag')

    def test_delete_tag(self):
        response = self.client.delete(reverse('tag-detail', kwargs={'pk': self.tag.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.count(), 0)
