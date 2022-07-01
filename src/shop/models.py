import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    class Meta:
        abstract = True

    create_datetime = models.DateTimeField(null=True, auto_now_add=True)
    last_update = models.DateTimeField(null=True, auto_now=True)


class Product(BaseModel):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    category = models.ForeignKey(
        to="shop.Category", verbose_name="category", on_delete=models.CASCADE, related_name="category"
    )
    title = models.CharField(verbose_name="Title", max_length=128)
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    price = models.DecimalField(verbose_name="Price", max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(default="default.png", upload_to="covers/", blank=True, null=True)

    def __str__(self):
        return f"{self.title}{self.category.name}"


class Category(BaseModel):
    name = models.CharField(max_length=128)
    description = models.CharField(verbose_name="description", max_length=128, null=True, blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        verbose_name = "Category of product"
        verbose_name_plural = "Category of products"

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('shop:category', kwargs={'cat_slug': self.slug})


class Order(BaseModel):
    customer = models.ForeignKey(
        to=get_user_model(),
        related_name="customer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(BaseModel):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(verbose_name="quantity in store", default=0, null=True, blank=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(BaseModel):
    customer = models.ForeignKey(
        to=get_user_model(),
        related_name="address",
        on_delete=models.SET_NULL,
        null=True
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=20, null=False)
    zipcode = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.address
