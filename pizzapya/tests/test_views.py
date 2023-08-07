from django.test import TestCase, Client
from django.urls import reverse
from pizzapya.models import Pizza, Topping


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')

    def test_index_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')