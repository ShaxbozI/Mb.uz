# Generated by Django 4.2.6 on 2023-10-22 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogs_slug_remove_blogs_tag_blogs_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='tag',
        ),
    ]
