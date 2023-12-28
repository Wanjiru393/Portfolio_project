# Generated by Django 5.0 on 2023-12-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pictures/'),
        ),
    ]