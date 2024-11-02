from django.urls import path

from . import views


urlpatterns = [
    path('kiosk', views.kiosk, name='kiosk'),
    path('cafemain', views.cafemain, name='cafemain'),
    path('paydone',views.paydone, name='paydone'),
    path('last', views.last, name='last'),
    path('fastfoodmain', views.fastfoodmain, name='fastfoodmain'),
    path('payment', views.payment, name="payment"),
    
    path('cafemain2', views.cafemain2, name='cafemain2'),
    path('start', views.start, name='start'),
    
]
