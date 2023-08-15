from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import catalog_list, contacts, product, item

app_name = CatalogConfig.name

urlpatterns = [
    path('', catalog_list),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', product, name='product'),
    path('item/<int:pk>', item, name='item'),

]