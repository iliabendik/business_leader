# Generated by Django 3.2.6 on 2021-09-17 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_city_choice_the_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='1', max_length=9)),
            ],
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(choices=[('moscow', 'moscow'), ('omsk', 'omsk')], max_length=50, verbose_name='Город'),
        ),
    ]