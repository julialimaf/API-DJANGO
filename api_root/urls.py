from django.contrib import admin
from django.urls import path, include
from api_rest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_rest.urls'), name='api_rest_urls'),
    path('', views.get_users, name='get_all_users'), 
     path('data/',views.user_manager, name='user_manager'),

]
