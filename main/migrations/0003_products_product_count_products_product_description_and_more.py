# Generated by Django 4.1 on 2022-08-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_products_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
