# Generated by Django 3.1 on 2020-09-27 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enso', '0034_auto_20200927_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergathering',
            name='status',
            field=models.CharField(choices=[('R', 'Requested'), ('I', 'Invited'), ('J', 'Joined')], default='J', max_length=1),
        ),
    ]
