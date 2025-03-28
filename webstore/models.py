from django.db import models
from django.contrib.auth.models import User


# Model for brands of mowers available
class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='brands/', default='', null=True, blank=True)

    def __str__(self):
        return self.name

# Model for Lawn mower models
class Mower_Model(models.Model):
    model_number = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='models/', default='', blank=True, null=True)
    model_name = models.CharField(max_length=50, default='N/A')

    def __str__(self):
        return self.model_number
    
    class Meta:
        verbose_name="Lawnmower Model"

# Model for mower parts
class Part(models.Model):
    part_number = models.CharField(max_length=20)
    mower_model = models.ManyToManyField(Mower_Model)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    part_name = models.CharField(max_length=50, default='N/A')
    image = models.ImageField(upload_to='parts/', default='', blank=True, null=True)
    description = models.CharField(max_length=200, default="No Description Available")


    def __str__(self):
        return self.part_number

    class Meta:
        verbose_name="Mower Part"

class Order(models.Model):
    option_1 = 'Processing'
    option_2 = 'Shipped'
    option_3 = 'Completed'
    
    choice =[
        (option_1,'Processing'),
        (option_2,'Shipped'),
        (option_3,'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=choice, default=option_1, max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order {self.id} by {self.user.username if self.user else 'Guest'}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"