from django.db import models

# Create your models here.
class Menu(models.Model):
    menuName = models.CharField(max_length=100, default="unknown")
    menuPrice = models.IntegerField(default=0)
    
    
class Cart(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    menuQuantity = models.IntegerField(default=0)
    option1 = models.CharField(max_length=100, default="핫")
    option2 = models.CharField(max_length=100, default="기본")
    totalPrice = models.IntegerField(default=0)
    
    
