# Generated by Django 5.0 on 2023-12-27 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chatapp', '0002_profile_full_name_profile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
    ]