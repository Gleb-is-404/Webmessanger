# Generated by Django 4.1.2 on 2024-03-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='files',
            field=models.FileField(default='f.txt', upload_to='uploads/'),
        ),
    ]
