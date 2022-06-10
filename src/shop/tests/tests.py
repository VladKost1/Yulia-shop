from django.contrib.auth.models import User
from django.test import TestCase

from shop.models import Basket, Category, Product


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="Vlad", password="12345")
        self.basket = Basket.objects.create(user=self.user)
        self.category = Category.objects.create(name="Smartphone", slug="smartphone")
        self.product = Product.objects.create(title="Iphone", price=17000, quantity="1", category=self.category)
        self.product2 = Product.objects.create(title="S", price=12000, quantity="1", category=self.category)
        self.basket.products.add(self.product)
        self.basket.products.add(self.product2)

    def test_category_name(self):
        self.assertEqual(self.category.name, "Smartphone")

    def test_basket_user(self):
        self.assertEqual(self.user, self.basket.user)

    def test_basket_product(self):
        product = self.basket.products.filter(title="Iphone").exists()
        self.assertTrue(product)

    def test_sum_products(self):
        self.assertEqual(self.basket.cost, 29000.00)

    def test_clear_basket(self):
        self.basket.clear_basket()
        self.assertEqual(self.basket.products.all().count(), 0)
