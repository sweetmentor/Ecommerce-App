from django.urls import path
from product.views import get_products 


urlpatterns = [
    path('', get_products, name='products'),
    # path('search/', search, name='search'),
    
]