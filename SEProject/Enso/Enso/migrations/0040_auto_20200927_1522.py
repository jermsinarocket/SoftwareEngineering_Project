# Generated by Django 3.1 on 2020-09-27 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Enso', '0039_auto_20200927_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'get_latest_by': 'date'},
        ),
    ]