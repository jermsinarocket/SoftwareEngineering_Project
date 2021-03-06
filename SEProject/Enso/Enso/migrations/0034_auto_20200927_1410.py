# Generated by Django 3.1 on 2020-09-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enso', '0033_gathering_chat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='gathering',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('F', 'Full'), ('C', 'Completed')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='usergathering',
            name='status',
            field=models.CharField(choices=[('R', 'Requested'), ('I', 'Invited'), ('J', 'Joined')], default='I', max_length=1),
        ),
    ]
