from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shop.views import (AccountView, CategoryView,
                        ProductDetailView,CategorySelectView, location, cart)

from shop import views

app_name = 'shop'

urlpatterns = [
    path("<uuid:uuid>/", ProductDetailView.as_view(), name="product_details"),
    path("categories/", CategoryView.as_view(), name="categories"),
    path("category/<slug:cat_slug>/", CategorySelectView.as_view(), name="category"),
    path("account/", AccountView.as_view(), name="account"),
    path("cart/", views.cart, name="cart"),
    # path("update_item/", views.updateItem, name="update_item"),
    path("location/", location, name="location"),
]

