# Generated by Django 3.0.4 on 2020-03-24 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_useraccount_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistprofile',
            name='photo',
            field=models.ImageField(null=True, upload_to='artists/profile_photos'),
        ),
    ]
