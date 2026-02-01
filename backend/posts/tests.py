from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Blog, Tag

class BlogFeatureTests(APITestCase):
    def setUp(self):
        # Setup: Create a user and a blog post
        self.user = User.objects.create_user(username='tester', password='password123')
        self.client.force_authenticate(user=self.user)
        self.blog = Blog.objects.create(
            title="Shortcut Test", 
            content="Testing likes, stars, and tags strictly.", 
            user=self.user
        )

    def test_dynamic_tag_shortcut(self):
        """Shortcut: Verify tags are created automatically on POST"""
        url = reverse('blog-list')
        data = {
            "title": "New Blog", 
            "content": "Content", 
            "category": "Tech", 
            "tags": ["AutoTag1", "AutoTag2"]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Tag.objects.filter(name="AutoTag1").exists())

    def test_interactions_shortcut(self):
        """Shortcut: Test Like and Star toggles in one go"""
        # Test Like
        like_url = reverse('toggle-like', kwargs={'pk': self.blog.pk})
        res = self.client.post(like_url)
        self.assertEqual(res.data['status'], 'liked')
        self.assertEqual(res.data['like_count'], 1)

        # Test Star
        star_url = reverse('toggle-star', kwargs={'pk': self.blog.pk})
        res = self.client.post(star_url)
        self.assertEqual(res.data['status'], 'starred')