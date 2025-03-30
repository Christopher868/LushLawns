from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Brand, Mower_Model, Part, Order, OrderItem, Info






# Class that turns part manytomany into checkboxes
class PartModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField : {'widget': CheckboxSelectMultiple}
    }

    search_fields = ['part_number']
# using search_fields to add search bars to admin page
class BrandModelAdmin(admin.ModelAdmin):
    search_fields = ['name']

class Mower_modelModelAdmin(admin.ModelAdmin):
    search_fields = ['model_number']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class InfoInline(admin.TabularInline):
    model = Info
    extra = 0

class OrderModelAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ('id', 'user', 'created_at', 'updated_at', 'status', 'total_price')
    readonly_fields =('id',)
    inlines = [OrderItemInline, InfoInline]

admin.site.register(Info)
admin.site.register(Order, OrderModelAdmin)
admin.site.register(Part, PartModelAdmin)
admin.site.register(Brand, BrandModelAdmin)
admin.site.register(Mower_Model, Mower_modelModelAdmin)