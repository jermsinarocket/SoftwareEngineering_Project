# Generated by Django 3.1 on 2020-11-04 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Enso', '0043_auto_20201103_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='rating',
            name='user_gathering',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='Enso.usergathering'),
        ),
    ]
