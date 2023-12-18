from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from app_site.serializers import AdvertSerializer
from app_site.models import Category, User, Advert

class DataBasexTests(APITestCase):
    def setUp(self):
        self.one_of_catgory = Category.objects.create(title="однушки")
        Category.objects.create(title="двушки")
        self.user_test = User.objects.create_user(
            name="Михаил",
            surname = "Елизаров",
            telephone = "88005553535",
            email="major@dofiga.com",
            password = "Krot_Dront"
        )
        self.user_test.save()
        self.advert = Advert.objects.create(
            advert="продам однушку срочно",
            price = 100000000,
            address = "беляево",
            rooms = 1,
            total_area = 22.8,
            kitchen_area = 14.8,
            living_area = 8,
            price_per_meter = 10000,
            ceiling_hight = 10.8,
            floor=10,
            prepayment=10,
            title = self.one_of_catgory
        )


    def test_category_list(self):
        response = self.client.get(reverse("categories"))
        self.assertEqual(response.status_code, 202)
        self.assertTrue({'id': 3, 'title': 'однушки'} in response.json())
        self.assertTrue({'id': 4, 'title': 'двушки'} in response.json())


    def test_advert_list(self):
        response = self.client.get(reverse("advrert"))
        self.assertEqual(response.status_code, 202)
        serialazers_data = AdvertSerializer(self.advert).data
        self.assertTrue(serialazers_data in response.data)


    def test_delete_advert(self):
        response = self.client.delete(reverse("sale-ad-delete", kwargs ={"pk": self.advert.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(reverse("advrert"))
        self.assertEqual(response.data, [])
