from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer

from accounts.models import Customer
from shop.models import Category, Product


class CategoryNestedSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class CustomerSerializer(ModelSerializer):
    permission_classes = [AllowAny]

    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "email", "is_staff"]

    def get_first_name(self):
        print(self.initial_data.get("first_name")),
        return self.initial_data.get("first_name")


class ProductListSerializer(ModelSerializer):
    permission_classes = [AllowAny]
    category = CategoryNestedSerializer(many=False)

    class Meta:
        model = Product
        fields = ["id", "title", "price", "create_datetime", "category"]


class ProductDetailSerializer(ModelSerializer):
    permission_classes = [AllowAny]

    class Meta:
        model = Product
        fields = ["title", "price", "category"]
