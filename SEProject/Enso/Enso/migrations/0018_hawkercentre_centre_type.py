# Generated by Django 3.1 on 2020-09-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enso', '0017_foodstore_cashless_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='hawkercentre',
            name='centre_type',
            field=models.CharField(choices=[('MK', 'Market'), ('HC', 'Hawker'), ('MHC', 'Market & Hawker')], default='HC', max_length=3),
        ),
    ]
