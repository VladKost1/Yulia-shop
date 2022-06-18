from django.urls import path

from shop.views import (AccountView, BasketDetailView, CategoryDetailView,
                        ProductDetailView)

urlpatterns = [
    # path("<uuid:uuid>/", ProductDetailView.as_view(), name="product_details"),
    path("products/", ProductDetailView.as_view(), name="products"),
    path("category/", CategoryDetailView.as_view(), name="category"),
    path("account/", AccountView.as_view(), name="account"),
    path("basket/", BasketDetailView.as_view(), name="basket"),
    # path("")
]
