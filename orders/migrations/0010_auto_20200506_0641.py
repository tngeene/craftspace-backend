# Generated by Django 3.0.4 on 2020-05-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_category_cover_photo'),
        ('orders', '0009_auto_20200506_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
