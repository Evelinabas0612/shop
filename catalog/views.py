from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core import cache
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm, CategoryForm
from catalog.models import Category, Product, Blog, Version
from catalog.service import get_categories_cache


# Create your views here.


def catalog_list(request):
    """Контроллер страницы catalog_list"""
    # if settings.CACHE_ENABLED:
    #     key = 'category_list'
    #     category_list = cache.get(key)
    #     if category_list is None:
    #         category_list = Category.objects.all()
    #         cache.set(key, category_list)
    # else:
    #     category_list = Category.objects.all()

    context = {
        'object_list': get_categories_cache(),
        'title': 'Главная'
    }
    return render(request, 'catalog\catalog_list.html', context)


# def categories(request):
#     """Контроллер страницы categories"""
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Категории'
#     }
#     return render(request, 'catalog\category_list.html', context)

class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }


# def contacts(request):
#     """Контроллер страницы contacts"""
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f"Имя: {name}\nТелефон: {phone}\nСообщение: {message}\n")
#     return render(request, 'catalog/contacts.html')

class ContactsPageView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {'title': 'Контакты'}


# def products(request):
#     """Контроллер страницы products"""
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Продукты'
#     }
#     return render(request, 'catalog\products.html', context)

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Продукты'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('version_set')
        return queryset


# def products_by_category(request, pk):
#     """Контроллер страницы products_by_category"""
#     category_item = Category.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(category_id=category_item.pk),
#         'title': f'Продукты {category_item.name}'
#
#     }
#     return render(request, 'catalog\products_by_category.html', context)


class ProductByCategoryListView(ListView):
    model = Product
    extra_context = {
        'title': 'Продукты'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['categoty_pk'] = category_item.pk
        context_data['title'] = f'Продукты {category_item.name}'
        return context_data


# def item(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object': product_item,
#         'title': product_item.name
#     }
#     return render(request, 'catalog/item_detail.html', context)

class ItemDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Продукты'
    }
    template_name = 'catalog/item_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.views_count += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')
    template_name = 'catalog/product_form.html'

    def test_func(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        if self.request.user.is_authenticated:
            self.object.owner = self.request.user
            self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')
    template_name = 'catalog/product_form.html'

    def test_func(self):
        return self.request.user.is_staff or self.get_object().owner == self.request.user

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.owner != self.request.user:
    #         raise Http404
    #     return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        if self.request.user.is_authenticated:
            self.object.owner = self.request.user
            self.object.save()

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')

    def test_func(self):
        return self.request.user.is_superuser or self.get_object().owner == self.request.user

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:categories')
    template_name = 'catalog/category_form.html'


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:categories')
    template_name = 'catalog/category_form.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('catalog:categories')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content',)
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'content',)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object

    # success_url = reverse_lazy('catalog:blog_detail')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view_blog', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog
    fields = ('title', 'content', 'is_published')

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


def toggle_activity(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.is_published:
        blog_item.is_published = False
    else:
        blog_item.is_published = True
    blog_item.save()
    return redirect(reverse('catalog:blog_list'))
