from django.db import models

# Create your models here.

class Store(models.Model):
    ownerName = models.CharField (max_length=50, null=False, default="") #ID와 같음
    storeName = models.CharField(max_length=50, null=False)
    minOrderPrice = models.PositiveIntegerField()
    #deliveryPriceList
    #menuList
    createdAt = models.DateField()
    storeAddress = models.CharField(max_length=150, null=False)
    storeTel = models.CharField(max_length=12)

    def __str__(self):
        return self.ownerName

class Order(models.Model):
    storeId = models.CharField(max_length=50) #class Store의 storeName과 동일 => 구현 중 필요없으면 삭제가능
    status = models.CharField(max_length=10)

class DeliveryPrice(models.Model):
    #Store에 DeliveryPrice가 여러 개 포함되는 관계 표현
    deliveryPriceList = models.ForeignKey(Store, on_delete=models.CASCADE)
    #
    orderPrice = models.PositiveIntegerField()
    deliveryPrice = models.PositiveIntegerField()