# Generated by Django 4.1.2 on 2024-01-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_users_email_address_users_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='password',
        ),
        migrations.AddField(
            model_name='users',
            name='email_address',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
