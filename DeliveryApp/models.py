from django.db import models
from datetime import datetime

# Create your models here.

class Store(models.Model):
    ownerName = models.CharField (max_length=50, null=False, default="") #로그인용 ID와 같음
    storeName = models.CharField(max_length=50, null=False)
    minOrderPrice = models.PositiveIntegerField()
    #
    #deliveryPriceList = models.ForeignKey(DeliveryPrice, on_delete=models.CASCADE, blank=True, null=True)
    #menuList = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menuList', blank=True, null=True)
    #
    createdAt = models.DateField()
    storeAddress = models.CharField(max_length=150, null=False)
    storeTel = models.CharField(max_length=12)

    def __str__(self):
        return self.ownerName

class DeliveryPrice(models.Model):
    #Store에 DeliveryPrice가 여러 개 포함되는 관계 표현
    deliveryPriceList = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)
    #
    orderPrice = models.PositiveIntegerField(default=0)
    deliveryPrice = models.PositiveIntegerField(default=0)

class User(models.Model):
    userEmail = models.EmailField()
    userName = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.userName

class Menu(models.Model):
    #
    menuList = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='menuList', default=1, null=True)
    #
    categoryName = models.CharField(max_length=50)
    menuName = models.CharField(max_length=50)
    menuDetail = models.TextField(default="")
    menuPrice = models.PositiveIntegerField(default=0)
    menuOrder = models.PositiveIntegerField(default=0)
    #
    #optionList = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='optionList', blank=True, null=True)
    #
    optionNumber = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.menuName

class Option(models.Model):
    #Menu에 Option이 여러 개 포함되는 관계 표현
    optionList = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='optionList', blank=True, null=True)
    #
    optionMenu = models.CharField(max_length=50)
    optionName = models.CharField(max_length=50)
    optionPrice = models.PositiveIntegerField(default=0)
    optionOrder = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.optionName

class Order(models.Model):
    storeId = models.CharField(max_length=50) #class Store의 userName과 동일
    status = models.CharField(max_length=10, default="접수대기")
    #
    #deliveryInfoList = models.ForeignKey(DeliveryInfo, on_delete=models.CASCADE, related_name='deliveryInfo', default=False)
    #
    deliveryTime = models.TimeField(blank=True, null=True)
    totalPrice = models.PositiveIntegerField(default=0)
    #orderPrice = models.PositiveIntegerField(default=0)
    deliveryPrice = models.PositiveIntegerField(default=0)
    totalPeople = models.PositiveIntegerField(default=0)
    createdAt = models.TimeField(default=datetime.now())
    isDelivery = models.BooleanField(default=False)

    def __str__(self):
        return self.storeId

class DeliveryInfo(models.Model):
    #
    deliveryInfoList = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='deliveryInfoList', blank=False, default="")
    #
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 유저 관계설정
    #menuList = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menuList2', blank=True, null=True)
    storeRequest = models.TextField()
    deliveryRequest = models.TextField()        