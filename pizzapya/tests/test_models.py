from django.test import TestCase
from pizzapya.models import Topping, Pizza


class TestModels(TestCase):
    def setUp(self):
        self.topping1 = Topping.objects.create(name="Salsa", category="sauce", img="", price=".59")
        self.topping2 = Topping.objects.create(name="Honey", category="sauce", img="", price=".49")
        self.pizza1 = Pizza.objects.create(name="Artichoke Pizza", price="23.99", img="", on_sale=False)
        self.pizza1.toppings.set([self.topping1.pk, self.topping2.pk])

    def test_topping_name(self):
        self.assertEqual(str(self.topping1), self.topping1.name)
        self.assertEqual(str(self.topping2), self.topping2.name)

    def test_pizza_name(self):
        self.assertEqual(str(self.pizza1), self.pizza1.name)