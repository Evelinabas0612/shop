from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import catalog_list, ContactsPageView, CategoryListView, \
    ProductListView, ProductByCategoryListView, ItemDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', catalog_list, name='catalog_list'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/', ProductListView.as_view(), name='products'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('<int:pk>/products_by_category/', ProductByCategoryListView.as_view(), name='products_by_category'),
    path('item/<int:pk>', ItemDetailView.as_view(), name='item'),

]