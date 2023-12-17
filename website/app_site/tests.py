from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase

class CategoryTests(APITestCase):
    def test_category_list(self):
        response = self.client.get(reverse("categories"))
        print(response)

# Create your tests here.
