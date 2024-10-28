from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
import json

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            menu_name = form.cleaned_data['menuName']
            menu_quantity = form.cleaned_data['menuQuantity']
            option1 = form.cleaned_data['option1']
            if form.cleaned_data['option2'] == "null":
                option2="기본"
            else:
                option2 = form.cleaned_data['option2']
                
            

            try:
                menu = Menu.objects.get(menuName=menu_name)
                
                try:
                    cart_item = Cart.objects.get(menu=menu, option1=option1, option2=option2)
                    cart_item.menuQuantity += 1
                    
    
                    cart_item.totalPrice += menu.menuPrice * menu_quantity
                    if option2 == "샷추가":
                        cart_item.totalPrice += 500 * menu_quantity
                    elif option2 == "2샷추가":
                        cart_item.totalPrice += 1000 * menu_quantity

                    cart_item.save()

                except Cart.DoesNotExist:
                    total_price = menu.menuPrice * menu_quantity
                    if option2 == "샷추가":
                        total_price += 500 * menu_quantity
                    elif option2 == "2샷추가":
                        total_price += 1000 * menu_quantity

                    Cart.objects.create(
                        menu=menu,
                        menuQuantity=menu_quantity,
                        option1=option1,
                        option2=option2,
                        totalPrice=total_price
                    )

                return JsonResponse({'message': 'Cart updated successfully!'}, status=200)
            
            except Menu.DoesNotExist:
                return JsonResponse({'error': 'Menu not found'}, status=404)
    else:
        form = CartForm()

    return JsonResponse({'error': 'Invalid form data'}, status=400)

@csrf_exempt
def detail(request, cartId):
    if request.method == 'DELETE':
        try:
            print(cartId)
            print(Cart.objects.filter(id=cartId))
            Cart.objects.filter(id=cartId).delete()
            return JsonResponse({'message': 'Cart deleted successfully!'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Menu not found'}, status=404)
    elif request.method == 'PUT':
        try:
            updateCart = Cart.objects.get(id=cartId)
            data = json.loads(request.body)
            updateQuantity = data.get('quantity', 0)
            
            updateCart.menuQuantity += updateQuantity
            updateCart.totalPrice += (updateQuantity * updateCart.menu.menuPrice)
            
            if updateCart.menuQuantity <= 0:
                updateCart.delete()
            else:
                updateCart.save()
            
            return JsonResponse({'message': 'Cart updated successfully!'}, status=200)
            
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Menu not found'}, status=404)

    
    
    

