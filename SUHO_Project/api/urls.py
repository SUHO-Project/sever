from django.urls import path

from . import views


urlpatterns = [
    path('cart/create', views.create, name='create_cart'),
    path('cart/<int:cartId>/', views.delete, name="cart_detail")
    
]
