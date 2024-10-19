from django import forms
from .models import Cart

class CartForm(forms.Form):
    menuName = forms.CharField(max_length=100, label="메뉴 이름")
    menuQuantity = forms.IntegerField(min_value=1, label="수량")
    option1 = forms.CharField(max_length=100, initial="핫", label="옵션 1")
    option2 = forms.CharField(max_length=100, initial="기본", label="옵션 2")