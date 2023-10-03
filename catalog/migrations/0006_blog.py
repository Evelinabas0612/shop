# Generated by Django 4.2.3 on 2023-08-20 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_slug_product_views_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=200, verbose_name='slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Cодержимое')),
                ('preview', models.ImageField(upload_to='previews/', verbose_name='Изображение')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=False, verbose_name='Признак публикации')),
                ('views_count', models.IntegerField(default=0, verbose_name='Kоличество просмотров')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
            },
        ),
    ]