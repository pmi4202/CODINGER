from django.contrib import admin
from .models import Store, Category, Order, User, DeliveryInfo, Menu, Option, DeliveryPrice, MenuSimple

# Register your models here.
admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(User)
admin.site.register(DeliveryInfo)
admin.site.register(Menu)
admin.site.register(MenuSimple)
admin.site.register(Option)
admin.site.register(DeliveryPrice)