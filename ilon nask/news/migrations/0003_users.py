# Generated by Django 4.1.2 on 2024-01-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_int_info_function_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=28)),
                ('surname', models.CharField(max_length=28)),
                ('email_address', models.EmailField(max_length=254)),
                ('points', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]