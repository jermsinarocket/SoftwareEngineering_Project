# Generated by Django 3.1 on 2020-09-17 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Enso', '0019_auto_20200917_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_profile', to='Enso.zipcode'),
        ),
    ]