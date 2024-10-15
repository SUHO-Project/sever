from django.urls import path

from . import views


urlpatterns = [
    path('', views.kiosk, name='kiosk'),
    path('cafemain', views.cafemain, name='cafemain'),
    path('fastfoodmain', views.fastfoodmain, name='fastfoodmain'),
    
]
