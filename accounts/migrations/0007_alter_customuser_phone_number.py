# Generated by Django 4.2.6 on 2023-11-03 13:32

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default=123456789123, max_length=13, validators=[accounts.models.CustomUser.validate_integer]),
        ),
    ]