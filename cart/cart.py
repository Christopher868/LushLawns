from django.contrib import messages
import ast

class Cart:
    def __init__(self,request):
        # Creates a session
        self.session = request.session

        # Gets a current session key if there is one
        cart = self.session.get('cart')

        # Creates a cart session key if one does not already exist
        if not cart:
            cart = self.session['cart'] = {}

        # Makes sure cart is always available
        self.cart = cart

    #Adds items to cart
    def add(self, part, quantity=1):
        part_id = str(part.id)

        if part_id in self.cart:
            if self.cart[part_id]['quantity'] >= part.quantity:
                return 1
            else:
                self.cart[part_id]['quantity'] += quantity

        else:
            self.cart[part_id] = {
                'name': part.part_name,
                'model': part.part_number,
                'price': str(part.price),
                'quantity':quantity
                }

        self.save()

    #Removes items from cart
    def remove(self, part_id):
        part_id = str(part_id)
        part = self.cart[part_id]

        if part_id in self.cart:
            if part['quantity'] > 1:
                part['quantity'] -= 1
                self.save()
            else:
                del self.cart[part_id]
                self.save()

    #Saves changes to Cart
    def save(self):
        self.session.modified = True


    def get_price(self, parts):
        total = 0

        for key in parts:
            total += (float(parts[key]['price']) * float(parts[key]['quantity']))
        return total

    

    # Get total items in cart
    def get_total_quantity(self):
        return sum(part['quantity'] for part in self.cart.values())

    def clear(self):
        self.session['cart'] = {}
        self.save()

    def get_cart_items(self):
        return self.cart

