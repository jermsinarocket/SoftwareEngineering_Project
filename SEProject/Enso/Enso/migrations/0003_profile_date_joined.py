# Generated by Django 3.1 on 2020-09-04 08:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Enso', '0002_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date joined'),
            preserve_default=False,
        ),
    ]
