from django.db import models


class Dish_image(models.Model):
    image = models.ImageField('Image:', upload_to='product_image/')


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
    image = models.ForeignKey(Dish_image, verbose_name='Image:', on_delete=models.CASCADE)





