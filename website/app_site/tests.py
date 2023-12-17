from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from app_site.models import Category

class CategoryTests(APITestCase):
    def setUp(self):
        Category.objects.create(title="однушки")
    def test_category_list(self):
        response = self.client.get(reverse("categories"))
        print(response.json())
        self.assertTrue({'id': 1, 'title': 'однушки'} in response.json())
# Create your tests here.
