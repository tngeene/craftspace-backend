# Generated by Django 3.0.4 on 2020-04-09 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_artistprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistprofile',
            name='user',
            field=models.OneToOneField(limit_choices_to={'membership_type': 'Artist'}, on_delete=django.db.models.deletion.CASCADE, related_name='artist_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='collectorprofile',
            name='user',
            field=models.OneToOneField(limit_choices_to={'membership_type': 'Artist'}, on_delete=django.db.models.deletion.CASCADE, related_name='collector_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
