from django.urls import path
from django.conf.urls import url
from .views import checkout

urlpatterns = [
  path('', checkout, name='checkout')
  
  ]

