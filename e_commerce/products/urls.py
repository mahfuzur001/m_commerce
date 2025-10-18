from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('add_product/', Add_product, name='add_product'),
    path('list_products/', list_products, name='list_products'),
]



