# Generated by Django 3.0.4 on 2020-03-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200314_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(to='orders.Cart'),
        ),
    ]