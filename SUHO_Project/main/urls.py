from django.urls import path

from . import views


urlpatterns = [
    path('kiosk', views.kiosk, name='kiosk'),
    path('cafemain', views.cafemain, name='cafemain'),
    path('paydone',views.paydone, name='paydone'),
    path('last', views.last, name='last'),
    path('payment', views.payment, name="payment"),
    
    path('cafemain2', views.cafemain2, name='cafemain2'),
    path('', views.start, name='start'),
    path('kiosk2', views.kiosk2, name='kiosk2'),
    path('payment2', views.payment2, name='payment2'),
    path('paydone2', views.paydone2, name='paydone2'),

    path('fastfoodmain', views.fastfoodmain, name='fastfoodmain'),
    path('fastfoodbuger', views.fastfoodbuger, name='fastfoodbuger'),
    path('buger_popup', views.buger_popup, name='buger_popup'),




    
]
