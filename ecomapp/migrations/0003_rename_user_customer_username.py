# Generated by Django 4.1.7 on 2023-03-29 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='username',
        ),
    ]
