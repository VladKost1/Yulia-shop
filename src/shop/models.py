from django.contrib.auth import get_user_model
from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    category = models.ForeignKey(
        to="shop.Category", verbose_name="category", on_delete=models.CASCADE, related_name="category"
    )
    title = models.CharField(verbose_name="Title", max_length=128)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    price = models.DecimalField(verbose_name="Price", max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name="quantity in store", default=0)
    image = models.ImageField(upload_to="media/covers", blank=True, null=True)

    def __str__(self):
        return f"{self.title}{self.category.name}"


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(verbose_name="description", max_length=128, null=True, blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        verbose_name = "Category of product"
        verbose_name_plural = "Category of products"

    def __str__(self):
        return f"{self.name}"


class Basket(models.Model):
    user = models.OneToOneField(
        to=get_user_model(),
        related_name="user",
        on_delete=models.CASCADE,
    )
    products = models.ManyToManyField(to="shop.Product", related_name="baskets")

    @property
    def cost(self):
        return sum(self.products.all().values_list("price", flat=True))

    def clear_basket(self):
        return self.products.through.objects.all().delete()
