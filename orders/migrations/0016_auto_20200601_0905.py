# Generated by Django 3.0.4 on 2020-06-01 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_cartitem_quantities'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=45, null=True),
        ),
    ]