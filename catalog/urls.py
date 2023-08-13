from itertools import product

from django.template import base
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import catalog_list, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', catalog_list),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', product, name='product'),

]