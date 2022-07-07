from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from shop.models import Category, Product


class TestAPI(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.product = Product.objects.create(
            title="test", category=Category.objects.create(name="name"), description="TEST"
        )

    def tearDown(self) -> None:
        self.product.delete()

    def test_product_list_wrong_user(self):
        result = self.client.get(reverse("api:product_details", kwargs={"uuid": self.product.uuid}))
        self.assertEqual(result.status_code, status.HTTP_401_UNAUTHORIZED)
