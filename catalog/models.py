
from django.db import models
from django.urls import reverse


from users.models import User

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, **NULLABLE, verbose_name='Категория')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')
    date_of_creation = models.DateField(verbose_name='Дата создания')
    date_last_modified = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения')

    views_count = models.IntegerField(default=0, verbose_name='Просмотры')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    owner = models.ForeignKey(User, on_delete=models.PROTECT, **NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.category}) ({self.price})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Blog(models.Model):
    '''Модель блог'''
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=200, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='Cодержимое')
    preview = models.ImageField(upload_to='previews/', verbose_name='Изображение')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Kоличество просмотров')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        """Slug"""
        return reverse('blog_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

class Version(models.Model):
    '''Модель версии продукта'''
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name='Продукт')
    version_number = models.CharField(max_length=50, verbose_name='Номер версии')
    version_name = models.CharField(max_length=250, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name='Активная версия')

    def __str__(self):
        return f'{self.product} ({self.version_number})'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'



