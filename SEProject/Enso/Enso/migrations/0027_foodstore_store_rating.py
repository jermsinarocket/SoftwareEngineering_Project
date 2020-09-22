# Generated by Django 3.1 on 2020-09-22 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enso', '0026_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodstore',
            name='store_rating',
            field=models.ManyToManyField(related_name='user_profile', through='Enso.Rating', to='Enso.Profile'),
        ),
    ]
