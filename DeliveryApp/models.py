from django.db import models
from datetime import datetime

# Create your models here.

class Store(models.Model):
    ownerName = models.CharField (max_length=50, null=False, default="") #로그인용 ID와 같음
    storeName = models.CharField(max_length=50, null=False)
    minOrderPrice = models.PositiveIntegerField()
    createdAt = models.DateField()
    storeAddress = models.CharField(max_length=150, null=False)
    storeTel = models.CharField(max_length=12)
    #categoryList = ArrayField(models.CharField(max_length=20, blank=True), size=20)#char형들의 배열

    def __str__(self):
        return self.ownerName

class Category(models.Model):
    categoryName = models.CharField(max_length=20, null=False, default="")
    orderMethod = models.CharField(max_length=10, null=False, default="개인메뉴")
    categoryList = models.ForeignKey(Store, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self):
        return self.categoryName

class DeliveryPrice(models.Model):
    #Store에 DeliveryPrice가 여러 개 포함되는 관계 표현
    deliveryPriceList = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)
    #
    orderPrice = models.PositiveIntegerField(default=0)
    deliveryPrice = models.PositiveIntegerField(default=0)

class Order(models.Model):
    storeId = models.CharField(max_length=50) #class Store의 userName과 동일
    status = models.CharField(max_length=10, default="접수대기")
    deliveryTime = models.PositiveIntegerField(default=30)
    totalPrice = models.PositiveIntegerField(default=0)
    #orderPrice = models.PositiveIntegerField(default=0)
    deliveryPrice = models.PositiveIntegerField(default=0)
    totalPeople = models.PositiveIntegerField(default=0)
    createdAt = models.TimeField(default=datetime.now())
    deliveryType = models.CharField(max_length=10, default = "단일배송")
    address = models.CharField(max_length=50, default="", blank=True, null=True)
    isDelivery = models.BooleanField(default=False)

    def __str__(self):
        return self.storeId

class MenuSimple(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE, blank = True, null = True)
    menuName = models.CharField(max_length=20)
    menuNumber = models.PositiveIntegerField(default=0)

class User(models.Model):
    userEmail = models.EmailField()
    userName = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.userName

class DeliveryInfo(models.Model):
    #
    deliveryInfoList = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='deliveryInfoList', blank=False, default="")
    #
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 유저 관계설정
    storeRequest = models.TextField()
    deliveryRequest = models.TextField() 

class Menu(models.Model):
    #
    menuList = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='storeMenu', default=1, null=True)
    menuList2 = models.ForeignKey(DeliveryInfo, on_delete=models.CASCADE, related_name='deliveryMenu', blank=True, null=True)
    #
    categoryName = models.CharField(max_length=50)
    menuName = models.CharField(max_length=50)
    menuDetail = models.TextField(default="")
    menuPrice = models.PositiveIntegerField(default=0)
    menuOrder = models.PositiveIntegerField(default=0)
    menuImage = models.ImageField(null=True)
    #optionNumber = models.PositiveIntegerField(default=0) #옵션 안하면 빼도 되는 항목

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