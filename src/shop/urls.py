from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from shop import views
from shop.views import (CategorySelectView, CategoryView,
                        ProductDetailView, cart, location, checkout, add_cart)

app_name = "shop"

urlpatterns = [
    path("<uuid:uuid>/", ProductDetailView.as_view(), name="product_details"),
    path("categories/", CategoryView.as_view(), name="categories"),
    path("category/<slug:cat_slug>/", CategorySelectView.as_view(), name="category"),
    path("cart/", views.cart, name="cart"),
    path("add-cart/<uuid:product>/", views.add_cart, name="add_cart"),
    path("delet-cart/", views.delete_cart, name="delete_cart"),
    # path("clear-cart/<uuid:product>/", ClearItemCart.as_view(), name="clear_cart"),
    path("location/", views.location, name="location"),
    path("checkout/", views.checkout, name="checkout"),

]
