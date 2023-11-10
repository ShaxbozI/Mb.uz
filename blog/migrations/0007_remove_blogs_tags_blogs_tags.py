# Generated by Django 4.2.6 on 2023-10-24 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogs_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='tags',
        ),
        migrations.AddField(
            model_name='blogs',
            name='tags',
            field=models.ManyToManyField(to='blog.tags'),
        ),
    ]