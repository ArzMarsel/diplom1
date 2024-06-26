# Generated by Django 5.0.3 on 2024-04-23 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_image/', verbose_name='Image:')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('info', models.TextField(verbose_name='Information')),
                ('price', models.FloatField(verbose_name='Price')),
                ('status', models.CharField(choices=[('done', 'Сделано'), ('none', 'Не сделано'), ('delivering', 'Доставляеться'), ('cooking', 'Готовиться'), ('accepted', 'Принят'), ('none', 'none')], max_length=30, verbose_name='Status:')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.dish_image', verbose_name='Image:')),
            ],
        ),
    ]
