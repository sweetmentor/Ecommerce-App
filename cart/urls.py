from django.urls import path
from django.conf.urls import url
from .views import view_cart


urlpatterns = [
  path('view_cart/', view_cart, name='view_cart'),
  
  ]