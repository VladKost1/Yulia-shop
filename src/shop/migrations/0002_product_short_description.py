# Generated by Django 3.2.13 on 2022-07-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Short Description'),
        ),
    ]
