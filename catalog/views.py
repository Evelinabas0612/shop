from django.shortcuts import render

# Create your views here.

def catalog_list(request):
    """Контроллер страницы catalog_list"""
    return render(request, 'catalog\catalog_list.html')


def contacts(request):
    """Контроллер страницы contacts"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя: {name}\nТелефон: {phone}\nСообщение: {message}\n")
    return render(request, 'catalog/contacts.html')