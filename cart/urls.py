from django.urls import path
from django.conf.urls import url
from .views import view_cart, add_to_cart, remove_from_cart


urlpatterns = [
  path('view_cart/', view_cart, name='view_cart'),
  path('add_to_cart/', add_to_cart, name='add_to_cart'),
  path('remove/', remove_from_cart, name = 'remove_from_cart')
  
  ]