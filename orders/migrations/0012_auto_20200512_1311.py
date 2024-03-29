# Generated by Django 3.0.4 on 2020-05-12 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_category_cover_photo'),
        ('orders', '0011_auto_20200506_0741'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_items', to=settings.AUTH_USER_MODEL)),
                ('products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(to='orders.CartItem'),
        ),
    ]
