from django.shortcuts import get_object_or_404
from product.models import Product
from decimal import Decimal


def get_cart_items_and_total(cart):
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
        
    return { 'cart_items': cart_items, 'total': cart_total }