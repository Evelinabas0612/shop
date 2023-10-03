# Generated by Django 4.2.3 on 2023-08-22 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Признак публикации'),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(max_length=50, verbose_name='Номер версии')),
                ('version_name', models.CharField(max_length=250, verbose_name='Название версии')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активная версия')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
