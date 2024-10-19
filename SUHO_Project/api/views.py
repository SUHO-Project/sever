from django.shortcuts import render, redirect
from django.http import HttpResponse
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
            option2 = form.cleaned_data['option2']

            try:
                # 입력된 메뉴 이름으로 Menu 객체를 찾음
                menu = Menu.objects.get(menuName=menu_name)
                
                # totalPrice는 메뉴 가격과 수량을 곱해서 계산
                total_price = menu.menuPrice * menu_quantity

                # Cart 객체 생성
                Cart.objects.create(
                    menu=menu,
                    menuQuantity=menu_quantity,
                    option1=option1,
                    option2=option2,
                    totalPrice=total_price
                )
                

                # 생성 후 장바구니 목록 페이지로 리다이렉트
                return HttpResponse("Cart created successfully!")
            
            except ObjectDoesNotExist:
                # 메뉴가 없을 경우 폼에 오류 메시지 추가
                form.add_error('menuName', '입력하신 메뉴가 존재하지 않습니다.')

    else:
        form = CartForm()

    return render(request, 'cafemain.html', {'form': form})
        