from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
import json
from .stt import *
import speech_recognition as sr

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

def createOther(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            menu_name = form.cleaned_data['menuName']
            menu_quantity = form.cleaned_data['menuQuantity']
            option1 = ""
            option2 = ""

            try:
                menu = Menu.objects.get(menuName=menu_name)
                try:
                    cart_item = Cart.objects.get(menu=menu, option1=option1, option2=option2)
                    cart_item.menuQuantity += 1
                    
    
                    cart_item.totalPrice += menu.menuPrice * menu_quantity

                    cart_item.save()

                except Cart.DoesNotExist:
                    total_price = menu.menuPrice * menu_quantity
                    
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

def createFastFood(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            menu_name = form.cleaned_data['menuName']
            menu_quantity = form.cleaned_data['menuQuantity']
            option1 = form.cleaned_data['option1']
            option2 = form.cleaned_data['option2']
            

            try:
                menu = Menu.objects.get(menuName=menu_name)
                
                try:
                    cart_item = Cart.objects.get(menu=menu, option1=option1, option2=option2)
                    cart_item.menuQuantity += 1
                    
    
                    cart_item.totalPrice += menu.menuPrice * menu_quantity
                    cart_item.totalPrice += Menu.objects.get(menuName=option1).menuPrice * menu_quantity
                    cart_item.totalPrice += Menu.objects.get(menuName=option2).menuPrice * menu_quantity
                    

                    cart_item.save()

                except Cart.DoesNotExist:
                    total_price = menu.menuPrice * menu_quantity
                    print(option1)
                    print(option2)
                    total_price += Menu.objects.get(menuName=option1).menuPrice * menu_quantity
                    total_price += Menu.objects.get(menuName=option2).menuPrice * menu_quantity

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
            
            updateCart.totalPrice += (updateQuantity * updateCart.menu.menuPrice)
            updateCart.menuQuantity += updateQuantity
            
            if updateCart.menuQuantity <= 0:
                updateCart.delete()
            else:
                updateCart.save()
            
            return JsonResponse({'message': 'Cart updated successfully!'}, status=200)
            
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Menu not found'}, status=404)
    
        
# 메인 실행
r = sr.Recognizer()
m = sr.Microphone()

@csrf_exempt
def speakApi(request):
    page = json.loads(request.body).get("page")
    message = json.loads(request.body).get('question')
    answer = ""
    speak(message)
    if page == "kiosk":
        answer = returnSpeak()
    elif page == "cafemain":
        answer = returnCafeMainSpeak()
    elif page == "popup1":
        answer = popup1()
    elif page == "popup2":
        answer = popup2()
    elif page == "popup3":
        answer = popup3()
    elif page == "payment":
        answer = payment()
    elif page == "payment2-1":
        answer = payment2_1()
    elif page == "payment2-2":
        answer = payment2_2()
    elif page == "payment2-3":
        answer = payment2_3()
    elif page == "receipt":
        answer = receipt()
    
    
    
    return JsonResponse({'message': answer}, status=200)
    
        

def returnSpeak():
    while True:
        answer = listen(r)
        if answer is not None:
            if "카페" in answer or "커피" in answer:
                return answer
            else:
                speak('없는 메뉴를 선택하셨어요. 다시 선택해 주세요.')
        else:
            speak('다시 말씀해 주세요.')

def returnCafeMainSpeak():
    while True:
        answer = listen(r)
        
        if answer is not None:
            answer.replace(" ","")
            if "아메리카노" in answer:
                return "americano"
            elif "카페라떼" in answer:
                return "cafe-latte"
            elif "바닐라라떼" in answer:
                return "valina-latte"
            elif "카라멜마끼아또" in answer:
                return "caramel-macchiato"
            elif "카페모카" in answer:
                return "cafe-mocha"
            elif "카푸치노" in answer:
                return "cappuccino"
            else:
                returnCafeMainSpeak('없는 메뉴를 선택하셨어요. 다시 선택해 주세요.')
        else:
            speak('다시 말씀해 주세요.')

def popup1():
    while True:
        answer = listen(r)
        if answer is not None:
            answer = answer.replace(" ", "")
            if "아이스" in answer or "차가" in answer:
                return "TemSelect2"
            elif "핫" in answer or "따뜻" in answer or "뜨거" in answer:
                return "TemSelect1"
            else:
                speak('없는 옵션을 선택하셨어요. 다시 선택해 주세요.')
        else:
            speak('다시 말씀해 주세요.')

def popup2():
    while True:
        answer = listen(r)
        if answer is not None:
            answer = answer.replace(" ", "")
            if "기본" in answer:
                return "기본"
            elif "연하" in answer:
                return "den1"
            elif "샷추가" in answer or "원샷추가" in answer:
                return "den3"
            elif "투샷추가" in answer or "2샷추가":
                return "den2"
            else:
                speak('없는 옵션을 선택하셨어요. 다시 선택해 주세요.')
        else:
            speak("다시 말씀해 주세요.")
    
def popup3():
    while True:
        answer = listen(r)
        
        if answer is not None:
            answer.replace(" ", "")
            if "네" in answer:
                return True
            elif "아니" in answer:
                return False
            else:
                speak('없는 옵션을 선택하셨어요. 다시 선택해 주세요.')
        else:
            speak('다시 말씀해 주세요.')
            
    
def payment():
    while True:
        answer = listen(r)
        
        if answer is not None:
            answer.replace(" ", "")
            if "네" in answer:
                return True
            elif "아니" in answer:
                return False
            else:
                speak('없는 옵션을 선택하셨어요. 다시 선택해 주세요.')
        else:
            speak('다시 말씀해 주세요.')

def payment2_1():
    while True:
        answer = listen(r)
        
        if answer is not None:
            answer.replace(" ", "")
            if "포장" in answer:
                return True
            elif "매장" in answer:
                return False
            else:
                speak('없는 옵션을 선택하셨어요. 다시 선택해 주세요.')
        else:
            speak('다시 말씀해 주세요.')

def payment2_2():
    while True:
        answer = listen(r)
        
        if answer is not None:
            answer.replace(" ", "")
            if "앱카드" in answer or "큐알" in answer or "qr" in answer:
                return "앱카드"
            elif "카드" in answer or "삼성" in answer:
                return "카드"
            elif "쿠폰" in answer:
                return "쿠폰"
            else:
                speak('없는 옵션을 선택하셨어요. 다시 선택해 주세요.')
        else:
            speak('다시 말씀해 주세요.')

def payment2_3():
    while True:
        answer = listen(r)
        
        if answer is not None:
            answer.replace(" ", "")
            if "네" in answer:
                return True
            elif "아니요" in answer:
                return False
            else:
                speak('없는 옵션을 선택하셨어요. 다시 선택해 주세요.')
        else:
            speak('다시 말씀해 주세요.')

def receipt():
    while True:
        answer = listen(r)
        if answer is not None:
            return True
        else:
            speak('다시 말씀해 주세요.')
