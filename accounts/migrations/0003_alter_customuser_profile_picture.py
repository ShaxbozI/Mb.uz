# Generated by Django 4.2.6 on 2023-10-25 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='images/default_picture_tands.png', upload_to='images/users'),
        ),
    ]
