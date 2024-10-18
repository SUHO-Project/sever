from django.db import models

# Create your models here.
class Menu(models.Model):
    menuId = models.AutoField(primary_key=True)
    menuName = models.CharField(max_length=100)
    menuPrice = models.IntegerField(default=0)
    
class Cart(models.Model):
    menu = models.ForeignKey(
        Menu,
        models.SET_NULL,
        blank=True,
        null=True
    )
    menuQuantity = models.IntegerField(default=0)
    
    
    class Meta:
        db_table = 'cart'
        verbose_name = '장바구니'
        verbose_name_plural = '장바구니'
