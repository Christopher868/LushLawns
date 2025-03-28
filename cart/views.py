from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from webstore.models import Part
from django.contrib import messages



# View that allows customers to view their cart
def cart_summary(request):
    cart = Cart(request)
    cart_items = cart.get_cart_items()

    sub_total_price = round(cart.get_price(cart_items), 2)
    tax = round(sub_total_price * 0.07, 2)
    total = sub_total_price + tax +14.99
    return render(request, 'cart.html', {'cart':cart_items, 'sub_total_price':sub_total_price, 'tax':tax, 'total':total })


# View that allows for customers to add products to their cart
def cart_add(request, part_id):
    cart = Cart(request)
    part = get_object_or_404(Part, id=part_id)
    value = cart.add(part)
    if value == 1:
        messages.success(request, ("Cannot add anymore to cart! There is only " + str(part.quantity) + " of that item available."))
    else:
        messages.success(request, ("Added to Cart!"))
    return redirect(request.META.get('HTTP_REFERER', '/')) 


# view that allows for customers to remove products from their cart
def cart_delete(request, part_id):
    cart = Cart(request)
    part = get_object_or_404(Part, id=part_id)
    cart.remove(part.id)
    return redirect('cart_summary')


def checkout(request):
    return render(request, 'checkout.html', {})

def cart_update(request):
    return render(request, 'cart.html', {})



