from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-models/', views.all_models, name='all_models'),
    path('all-parts/', views.all_parts, name='all_parts'),
    path('models/<str:brand_name>', views.models, name='models'),
    path('parts/<str:model_num>', views.parts, name='parts'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('part/<str:part_num>', views.part_info, name='part-info'),
    path('search/', views.search, name='search'),
]
