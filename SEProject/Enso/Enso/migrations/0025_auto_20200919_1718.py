# Generated by Django 3.1 on 2020-09-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enso', '0024_foodstore_cuisine_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodstore',
            name='store_image',
            field=models.TextField(blank=True, default='store-default-pic', null=True),
        ),
    ]
