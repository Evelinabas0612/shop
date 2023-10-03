from django.contrib import admin

from catalog.models import Product, Category, Version


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', 'description',)
    list_filter = ('category', 'is_published')
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'version_number', 'version_name',)
    list_filter = ('product', 'version_name',)
