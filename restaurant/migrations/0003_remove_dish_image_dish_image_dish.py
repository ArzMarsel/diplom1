# Generated by Django 5.0.3 on 2024-05-07 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_connect'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='image',
        ),
        migrations.AddField(
            model_name='dish_image',
            name='dish',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.dish'),
            preserve_default=False,
        ),
    ]