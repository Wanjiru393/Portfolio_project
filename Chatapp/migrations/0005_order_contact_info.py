# Generated by Django 5.0 on 2023-12-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatapp', '0004_order_transaction_code_alter_profile_profile_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='contact_info',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
