from django.contrib import admin
from .models import Store, Order, User, DeliveryInfo, Menu, Option, DeliveryPrice 

# Register your models here.
admin.site.register(Store)
admin.site.register(Order)
admin.site.register(User)
admin.site.register(DeliveryInfo)
admin.site.register(Menu)
admin.site.register(Option)
admin.site.register(DeliveryPrice)