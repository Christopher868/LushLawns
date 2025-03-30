from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from webstore.models import Part, Order, OrderItem
from django.contrib import messages
from webstore.forms import Shipping



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
    cart = Cart(request)
    items = cart.get_cart_items()
    price = cart.get_price(items)
    if len(items) == 0:
        messages.success(request, ("No items in cart checkout unsuccessful!"))
        return redirect('cart_summary')
    
    if request.method == "POST":
        form = Shipping(request.post)
        if form.is_valid():
            form.save()

    else:
        form = Shipping()
        return render(request, 'checkout.html', {'form':form, 'price':price})

def cart_update(request):
    return render(request, 'cart.html', {})


# View that generates an order for your purchase
def create_order(request):
    cart = Cart(request)
    items = cart.get_cart_items()
    
    user = request.user if request.user.is_authenticated else None
    order = Order.objects.create(user=user, total_price=cart.get_price(items))

    for key in items:
        OrderItem.objects.create(
            order=order,
            part = Part.objects.get(id=items[key]['id']),
            price = items[key]['price'],
            quantity = items[key]['quantity']
        )

    cart.clear()
    return redirect('order_success')


def order_success(request):
    return render(request, 'order_success.html', {})
