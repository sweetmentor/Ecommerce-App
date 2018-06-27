from django.shortcuts import render, redirect, get_object_or_404, HttpResponse 
from product.models import Product
# Create your views here.
def view_cart(request):
    cart = request.session.get('cart', {})
    
    cart_total = 0
    cart_items = []
    
    for key in cart:
        product = get_object_or_404(Product, pk=key)
        quantity = cart[key]
        
        cart_item = {
            'product': product,
            'quantity': quantity,
            'sub_total': product.price * quantity
            
        }
        
        cart_items.append(cart_item)
        cart_total += cart_item['sub_total']
    
         
    return render(request, "cart/cart.html", {'cart_items': cart_items, 'total': cart_total})
    
    
def remove_from_cart(request):
     id = request.POST['product_id']
     product = get_object_or_404(Product, pk=id)
     cart = request.session.get('cart', {})
     del cart[id]
     request.session['cart'] = cart
     return  redirect('view_cart')





def add_to_cart(request):
    # Get the product we're adding
    id = request.POST['product_id']
    product = get_object_or_404(Product, pk=id)
    
    # Get the current Cart
    cart = request.session.get('cart', {})
    
    # Update the Cart
    cart[id] = cart.get(id, 0) + 1
    
    # Save the Cart back to the session
    request.session['cart'] = cart
    
    #  Redirect somewhere
    
    return HttpResponse(cart[id])
  







