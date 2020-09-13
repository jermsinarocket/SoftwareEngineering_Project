# Generated by Django 3.1 on 2020-09-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enso', '0004_auto_20200910_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.TextField(blank=True, default='user-default-profile-pic', null=True),
        ),
    ]