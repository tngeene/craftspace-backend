# Generated by Django 3.0.4 on 2020-05-31 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_cartitem_quantities'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpesapayment',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_payment', to='orders.Order'),
        ),
    ]
