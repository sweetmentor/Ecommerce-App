from django.shortcuts import render 
from .models import Product

# Create your views here ----- products.
def get_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products': products})
    
    
# def search(request):        
#     if request.method == 'GET': # this will be GET now      
#         product_name =  request.GET.get('search') # do some research what it does       
#         try:
#             status = Add_prod.objects.filter(productname__icontains=product_name) # filter returns a list so you might consider skip except part
#         return render(request, "products/search.html",{"product":status})
#     else:
#         return render(request, "products/search.html",{})
    

    
    
   