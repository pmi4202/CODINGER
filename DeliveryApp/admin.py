from django.contrib import admin
from .models import Store, Category, Order, AppUser, DeliveryInfo, Menu, Option, DeliveryPrice, MenuSimple

# Register your models here.
admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(AppUser)
admin.site.register(DeliveryInfo)
admin.site.register(Menu)
admin.site.register(MenuSimple)
admin.site.register(Option)
admin.site.register(DeliveryPrice)