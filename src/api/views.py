from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import (DestroyAPIView, ListCreateAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from accounts.models import Customer
from api.serializers import (CategoryNestedSerializer, CustomerSerializer,
                             ProductDetailSerializer, ProductListSerializer)
from shop.models import Category, Product


class UserViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductListView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def get_object(self):
        return Product.objects.get(product__uuid=self.kwargs.get("uuid"))


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "uuid"


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "uuid"


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryNestedSerializer
