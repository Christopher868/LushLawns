from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-models/', views.all_models, name='all_models'),
    path('all-parts/', views.all_parts, name='all_parts'),
]
