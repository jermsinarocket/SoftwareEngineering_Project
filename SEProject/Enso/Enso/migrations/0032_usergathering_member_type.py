# Generated by Django 3.1 on 2020-09-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enso', '0031_gathering_no_pax'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergathering',
            name='member_type',
            field=models.CharField(choices=[('H', 'Host'), ('M', 'Member')], default='M', max_length=1),
        ),
    ]
