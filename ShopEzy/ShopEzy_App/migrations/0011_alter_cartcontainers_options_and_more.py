# Generated by Django 5.0.1 on 2024-01-17 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopEzy_App', '0010_alter_products_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartcontainers',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='shoppingcarts',
            options={'managed': True},
        ),
    ]
