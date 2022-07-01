from django.contrib import admin

from shop.models import Category, Order, OrderItem, Product, ShippingAddress

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
