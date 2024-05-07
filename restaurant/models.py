from django.contrib.auth.models import User
from django.db import models


class Dish(models.Model):
    Choices_list = (
        ('done', 'Сделано'),
        ('none', 'Не сделано'),
        ('delivering', 'Доставляеться'),
        ('cooking', 'Готовиться'),
        ('accepted', 'Принят'),
        ('none', 'none')
    )
    name = models.CharField('Name', max_length=30)
    info = models.TextField('Information')
    price = models.FloatField('Price')
    status = models.CharField(verbose_name='Status:', max_length=30, choices=Choices_list)


class Dish_image(models.Model):
    image = models.ImageField('Image:', upload_to='product_image/')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)


class Connect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
