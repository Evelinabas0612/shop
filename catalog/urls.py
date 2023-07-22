from django.urls import path

from catalog.views import catalog_list, contacts


urlpatterns = [
    path('', catalog_list),
    path('contacts/', contacts)
]