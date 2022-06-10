# Generated by Django 3.2.13 on 2022-06-09 16:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128)),
                ("description", models.CharField(max_length=128, verbose_name="description")),
                ("slug", models.SlugField(max_length=200, unique=True)),
            ],
            options={
                "verbose_name": "Category of product",
                "verbose_name_plural": "Category of products",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=128, verbose_name="Title")),
                ("description", models.TextField(blank=True, verbose_name="Description")),
                ("price", models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name="Price")),
                ("quantity", models.PositiveIntegerField(default=0, verbose_name="quantity in store")),
                ("image", models.ImageField(blank=True, upload_to="media/covers")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category",
                        to="shop.category",
                        verbose_name="category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.CreateModel(
            name="Basket",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("products", models.ManyToManyField(related_name="baskets", to="shop.Product")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, related_name="user", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
