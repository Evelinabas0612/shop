from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    """Модель Category"""
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(max_length=500, verbose_name='Описание')


    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Create your models here.
class Product(models.Model):
    """Модель Product"""
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(max_length=500, verbose_name='Описание')
    photo = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категория')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за покупку')
    date_of_creation = models.DateField(verbose_name='Дата создания')
    date_last_modified = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} ({self.category}) ({self.price})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
