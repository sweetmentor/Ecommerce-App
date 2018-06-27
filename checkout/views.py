from django.shortcuts import render, get_object_or_404
from .forms import MakePaymentForm, OrderForm
from product.models import Product
# Create your views here.


def checkout(request):
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

    
    
    order_form = OrderForm()
    payment_form = MakePaymentForm()

    return render(request, "checkout/checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'cart_items': cart_items, 'total': cart_total})
