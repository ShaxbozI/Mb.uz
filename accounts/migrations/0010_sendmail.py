# Generated by Django 4.2.7 on 2023-11-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_customuser_status_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tite', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('teacher_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
