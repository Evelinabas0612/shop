from django.shortcuts import render

from catalog.models import Category, Product


# Create your views here.

def catalog_list(request):
    """Контроллер страницы catalog_list"""
    context = {
        'object_list': Category.objects.all(),
        'title': 'Главная'
    }
    return render(request, 'catalog\catalog_list.html', context)


def contacts(request):
    """Контроллер страницы contacts"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя: {name}\nТелефон: {phone}\nСообщение: {message}\n")
    return render(request, 'catalog/contacts.html')

def product(request, pk):
    """Контроллер страницы product"""
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=category_item.pk),
        'title': f'Продукты {category_item.name}'

    }
    return render(request, 'catalog\product.html', context)


def item(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object': product_item,
        'title': product_item.name
    }
    return render(request, 'catalog/item.html', context)