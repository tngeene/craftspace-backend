# Generated by Django 3.0.4 on 2020-08-23 18:06

from django.db import migrations, models
import products.validators


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.PositiveIntegerField(default=1, validators=[products.validators.validate_quantities_available]),
        ),
    ]
