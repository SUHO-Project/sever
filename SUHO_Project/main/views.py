from django.shortcuts import render
from api.models import *

# Create your views here.
def kiosk(request):
    Cart.objects.all().delete()
    return render(request,'kiosk.html')

def cafemain(request):
    carts = Cart.objects.all()
    
    total = 0
    for cart in carts:
        total += cart.totalPrice
    
    return render(request,'cafemain.html', {'carts':carts, 'total':total})

def paydone(request):
    return render(request, 'paydone.html')

def last(requset):
    return render(requset, 'last.html')

def fastfoodmain(request):
    return render(request, 'fastfoodmain.html')

def payment(request):
    return render(request, 'payment.html')
