from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.get_users, name='get_all_users'),  
    path('data/',views.user_manager, name='user_manager'),
    path('cadastro/', views.cadastro, name='user_cadastro'),
    
]
