from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    path('add/<str:part_id>/', views.cart_add, name='cart_add'),
    path('delete/<int:part_id>/', views.cart_delete, name='cart_delete'),
    path('update', views.cart_update, name='cart_update'),
    path('checkout/', views.checkout, name='checkout'),
]
