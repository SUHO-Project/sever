from django.urls import path

from . import views


urlpatterns = [
    path('cart/create', views.create, name='create_cart'),
    path('cart/<int:cartId>/', views.detail, name="cart_detail"),
    path('stt/speak', views.speakApi, name="stt_speak"),
    path('cart/fastfood/create', views.createFastFood, name='create_fastfood_cart')
]
