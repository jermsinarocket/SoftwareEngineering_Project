# Generated by Django 3.1 on 2020-11-04 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enso', '0050_auto_20201105_0457'),
    ]

    operations = [
        migrations.AddField(
            model_name='gathering',
            name='receipt',
            field=models.TextField(blank=True, default='receipt-default-pic', null=True),
        ),
    ]
