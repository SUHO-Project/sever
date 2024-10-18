from django.shortcuts import render

# Create your views here.
def kiosk(request):
    return render(request,'kiosk.html')

def cafemain(request):
    return render(request,'cafemain.html')

def paydone(request):
    return render(request, 'paydone.html')

def last(requset):
    return render(requset, 'last.html')

def fastfoodmain(request):
    return render(request, 'fastfoodmain.html')

def payment(request):
    return render(request, 'payment.html')