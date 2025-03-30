from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    path('add/<str:part_id>/', views.cart_add, name='cart_add'),
    path('delete/<int:part_id>/', views.cart_delete, name='cart_delete'),
    path('checkout/', views.checkout, name='checkout'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_success/', views.order_success, name='order_success'),
]
