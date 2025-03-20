from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Brand, Mower_Model, Part 


admin.site.register(Brand)
admin.site.register(Mower_Model)


# Class that turns part manytomany into checkboxes
class PartModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField : {'widget': CheckboxSelectMultiple}
    }

admin.site.register(Part, PartModelAdmin)