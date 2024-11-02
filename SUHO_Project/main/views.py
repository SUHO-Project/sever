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

def cafemain2(request):
    total = 0
    carts = Cart.objects.all()

    for cart in carts:
        total += cart.totalPrice
    return render(request,'cafemain2.html', {'carts':carts, 'total':total})




def start(request):
    return render(request, 'start.html')

def kiosk2(request):
    Cart.objects.all().delete()
    return render(request,'kiosk2.html')

def payment2(request):
    return render(request, 'payment2.html')

def paydone2(request):
    return render(request, 'paydone2.html')



def fastfoodmain(request):
    return render(request, 'fastfoodmain.html')

def fastfoodbuger(request):
    carts = Cart.objects.all()
    
    total = 0
    for cart in carts:
        total += cart.totalPrice
    return render(request,'fastfoodbuger.html')

def buger_popup(request):
    return render(request, 'buger_popup.html')






