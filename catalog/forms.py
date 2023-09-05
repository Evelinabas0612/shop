from django import forms
from django.forms import ModelForm

from catalog.models import Product, Version, Category

# слова исключения
EXCEPTION_WORDS = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')


class StyleFormMixin:
    """Класс стилизации ручной метод"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        # fields = ('name', 'description', 'category')
        exclude = ('date_last_modified', 'views_count', 'slug')

    def clean_name(self):
        """Запрещенные слова при создании товара для поля name"""
        cleaned_data = self.cleaned_data['name'].lower()
        if cleaned_data in EXCEPTION_WORDS:
            raise forms.ValidationError('Название товара содержит запрещенные слова')
        return cleaned_data

    def clean_description(self):
        """Запрещенные слова при создании товара для поля description"""
        cleaned_data = self.cleaned_data['description'].lower()
        if cleaned_data in EXCEPTION_WORDS:
            raise forms.ValidationError('Описание товара содержит запрещенные слова')
        return cleaned_data


class CategoryForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')

    def clean_name(self):
        """Запрещенные слова при создании категории для поля name"""
        cleaned_data = self.cleaned_data['name'].lower()
        if cleaned_data in EXCEPTION_WORDS:
            raise forms.ValidationError('Название категории содержит запрещенные слова')
        return cleaned_data

    def clean_description(self):
        """Запрещенные слова при создании категории для поля description"""
        cleaned_data = self.cleaned_data['description'].lower()
        if cleaned_data in EXCEPTION_WORDS:
            raise forms.ValidationError('Описание категории содержит запрещенные слова')
        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
