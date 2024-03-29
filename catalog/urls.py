from django.urls import path
from django.views.decorators.cache import never_cache, cache_page

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import catalog_list, ContactsPageView, CategoryListView, \
    ProductListView, ProductByCategoryListView, ItemDetailView, ProductCreateView, ProductUpdateView, BlogCreateView, \
    BlogListView, BlogDetailView, \
    BlogUpdateView, BlogDeleteView, toggle_activity, ProductDeleteView, CategoryCreateView, CategoryUpdateView, \
    CategoryDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', catalog_list, name='catalog_list'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/', ProductListView.as_view(), name='products'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('<int:pk>/products_by_category/', ProductByCategoryListView.as_view(), name='products_by_category'),
    #path('item/<int:pk>', ItemDetailView.as_view(), name='item'),
    path('item/<int:pk>/', cache_page(60)(views.ItemDetailView.as_view()), name='item'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view_blog'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('published/<int:pk>/', toggle_activity, name='toggle_activity'),
   # path('products_by_category/create/', ProductCreateView.as_view(), name='create_product'),
    path('products_by_category/create/', never_cache(views.ProductCreateView.as_view()), name='create_product'),
    #path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('products/<int:pk>/update/', never_cache(views.ProductUpdateView.as_view()), name='update_product'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('categories/create/', CategoryCreateView.as_view(), name='create_category'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='update_category'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='delete_category'),
]
