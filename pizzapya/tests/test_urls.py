from django.test import TestCase
from django.urls import reverse, resolve
from pizzapya.views import index


class TestURLs(TestCase):
    def test_homepage_exists(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)
