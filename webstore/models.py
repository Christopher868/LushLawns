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
        verbose_name="Lawnmower"

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
        verbose_name="Part"

class Order(models.Model):
    option_1 = 'Processing'
    option_2 = 'Shipped'
    option_3 = 'Completed'
    option_4 = 'Failed'
    option_5 = 'Cancelled'
    
    choice =[
        (option_1,'Processing'),
        (option_2,'Shipped'),
        (option_3,'Completed'),
        (option_4,'Failed'),
        (option_5,'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=choice, default=option_1, max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order {self.id} by User: {self.user.username if self.user else 'Guest'}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Part #{self.part.part_number} x {self.quantity}  in Order {self.order.id} | Total: ${self.get_total_price()}"
    
class Info(models.Model):

    STATE_CHOICES = (
        ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'),
        ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'),
        ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'),
        ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'),
        ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'),
        ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'),
        ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
        ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'),
        ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'),
        ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'),
        ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'),
        ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'),
        ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'),
        ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'),
        ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'),
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE , editable=False, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    street = models.CharField(max_length=100)
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    zipcode = models.CharField(max_length=9)
    card =  models.DecimalField(max_digits=16, decimal_places=0 )
    security_code = models.DecimalField(max_digits=3, decimal_places=0)
    expiration = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural="Shipping Info"

    def __str__(self):
        if self.order:
           return str(self.order)
        else:
            return f'{self.first_name} {self.last_name}'

        


#Model to store session data
class UserSession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    session_data = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Session for {self.user.username}"
