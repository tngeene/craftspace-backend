# Generated by Django 3.0.4 on 2020-07-21 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200721_2226'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0017_auto_20200604_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='customorder',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_items', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='customorder',
            name='artist',
            field=models.ForeignKey(limit_choices_to={'membership_type': 'Artist'}, on_delete=django.db.models.deletion.CASCADE, related_name='cust_orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customorder',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='custom_orders/images'),
        ),
        migrations.AlterField(
            model_name='customorder',
            name='medium',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_orders', to='products.Medium'),
        ),
        migrations.AlterField(
            model_name='customorder',
            name='requested_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='custom_orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]