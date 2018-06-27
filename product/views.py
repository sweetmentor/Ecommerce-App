from django.shortcuts import render 
from .models import Product

# Create your views here ----- products.
def get_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products': products})
    

    
    
   