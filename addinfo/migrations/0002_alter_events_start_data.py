# Generated by Django 4.2.7 on 2023-11-10 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('addinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='start_data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
