from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='brands/', default='', null=True, blank=True)

    def __str__(self):
        return self.name

class Mower_Model(models.Model):
    model_number = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='models/', default='', blank=True, null=True)
    model_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.model_number
    
    class Meta:
        verbose_name="Lawnmower Model"