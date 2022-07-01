from django.contrib import admin

from shop.models import OrderItem, Category, Product, ShippingAddress, Order

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

