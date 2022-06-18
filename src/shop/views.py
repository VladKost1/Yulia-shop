from django.shortcuts import render
from django.views.generic import DetailView, ListView

from accounts.models import Customer
from shop.models import Basket, Category, Product


class IndexView(ListView):
    template_name = "index.html"
    model = Product


class ProductDetailView(ListView):
    template_name = "products.html"
    model = Product


class CategoryDetailView(ListView):
    template_name = "category.html"
    model = Category


class BasketDetailView(ListView):
    template_name = "basket.html"
    model = Basket


class AccountView(ListView):
    template_name = "account.html"
    model = Customer
