# Generated by Django 4.2.6 on 2023-10-30 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='coure_name',
            new_name='course_name',
        ),
    ]