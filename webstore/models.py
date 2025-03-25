from django.db import models


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
    part_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='parts/', default='', blank=True, null=True)
    description = models.CharField(max_length=200, default="No Description Available")


    def __str__(self):
        return self.part_number

    class Meta:
        verbose_name="Mower Part"
   