from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *

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
                # 입력된 메뉴 이름으로 Menu 객체를 찾음
                menu = Menu.objects.get(menuName=menu_name)
                
                # totalPrice는 메뉴 가격과 수량을 곱해서 계산
                total_price = menu.menuPrice * menu_quantity
                
                if option2 == "샷추가":
                    total_price += 500
                    
                elif option2 == "2샷추가":
                    total_price += 1000

                # Cart 객체 생성
                Cart.objects.create(
                    menu=menu,
                    menuQuantity=menu_quantity,
                    option1=option1,
                    option2=option2,
                    totalPrice=total_price
                )
                

                # 생성 후 장바구니 목록 페이지로 리다이렉트
                return JsonResponse({'message': 'Cart created successfully!'}, status=200)
            
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'Menu not found'}, status=404)
    else:
        form = CartForm()

    return JsonResponse({'error': 'Invalid form data'}, status=400)

@csrf_exempt
def delete(request, cartId):
    try:
        print(cartId)
        print(Cart.objects.filter(id=cartId))
        Cart.objects.filter(id=cartId).delete()
        return JsonResponse({'message': 'Cart deleted successfully!'}, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Menu not found'}, status=404)
    

