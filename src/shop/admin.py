from django.contrib import admin

from shop.models import Basket, Category, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Basket)
