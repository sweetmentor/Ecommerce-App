from django.shortcuts import render, redirect, get_object_or_404, HttpResponse 
from product.models import Product
from .utils import get_cart_items_and_total

# Create your views here.
def view_cart(request):
    cart = request.session.get('cart', {})
    context = get_cart_items_and_total(cart)
    return render(request, "cart/cart.html", context)


def remove_from_cart(request): 
    id = request.POST['product_id']
    product = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    if id in cart:
        # Subtract 1 from the quantity
        cart[id] -= 1
        # If the quantity is now 0, then delete the item
        if cart[id] == 0:
            del cart[id]
    request.session['cart'] = cart
    return redirect('view_cart')





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
  







