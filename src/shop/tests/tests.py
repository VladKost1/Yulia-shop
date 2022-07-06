from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import Customer
from shop.models import Category, Order, OrderItem, Product


class TestModels(TestCase):
    def setUp(self):
        self.user = Customer.objects.create(email="Vlad@vlad.com", password="12345")
        self.category = Category.objects.create(name="Smartphone", slug="smartphone")
        self.product = Product.objects.create(title="Iphone", price=17000, category=self.category)
        self.product2 = Product.objects.create(title="Samsung", price=12000, category=self.category)

    def test_category_name(self):
        self.assertEqual(self.category.name, "Smartphone")
