# Generated by Django 3.2.6 on 2021-09-12 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_city_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='city',
            new_name='name',
        ),
    ]
