from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Brand, Mower_Model, Part 






# Class that turns part manytomany into checkboxes
class PartModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField : {'widget': CheckboxSelectMultiple}
    }

    search_fields = ['part_number']

class BrandModelAdmin(admin.ModelAdmin):
    search_fields = ['name']

class Mower_modelModelAdmin(admin.ModelAdmin):
    search_fields = ['model_number']

admin.site.register(Part, PartModelAdmin)
admin.site.register(Brand, BrandModelAdmin)
admin.site.register(Mower_Model, Mower_modelModelAdmin)