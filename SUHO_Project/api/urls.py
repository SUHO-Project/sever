from django.urls import path

from . import views


urlpatterns = [
    path('cart/create', views.create, name='create_cart'),
    
]
