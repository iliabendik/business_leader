# Generated by Django 3.2.6 on 2021-09-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_category_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.SlugField(default='', max_length=100, verbose_name='Url'),
        ),
    ]
