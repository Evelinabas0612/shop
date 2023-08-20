from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import catalog_list, ContactsPageView, CategoryListView, \
    ProductListView, ProductByCategoryListView, ItemDetailView, BlogCreateView, BlogListView, BlogDetailView, \
    BlogUpdateView, BlogDeleteView, toggle_activity

app_name = CatalogConfig.name

urlpatterns = [
    path('', catalog_list, name='catalog_list'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/', ProductListView.as_view(), name='products'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('<int:pk>/products_by_category/', ProductByCategoryListView.as_view(), name='products_by_category'),
    path('item/<int:pk>', ItemDetailView.as_view(), name='item'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view_blog'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('published/<int:pk>/', toggle_activity, name='toggle_activity')

]