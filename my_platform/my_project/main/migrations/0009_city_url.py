# Generated by Django 3.2.6 on 2021-09-11 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210911_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='url',
            field=models.SlugField(default='', max_length=100, unique=True, verbose_name='Url'),
        ),
    ]