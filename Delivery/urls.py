"""Delivery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import DeliveryApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DeliveryApp.views.store_login, name='store_login'),
    path('/home', DeliveryApp.views.store_home, name='store_home'),
    path('/menu', DeliveryApp.views.store_menu, name='store_menu'),
    path('/order', DeliveryApp.views.store_order, name='store_order'),
    path('/order/detail', DeliveryApp.views.store_order_detail, name='store_order_detail'),
    path('/order/add', DeliveryApp.views.store_order_add, name='store_order_add'),
    path('/order/delete', DeliveryApp.views.store_order_delete, name='store_order_delete'),
    path('/order2', DeliveryApp.views.store_order2, name='store_order2'),
    path('/order3', DeliveryApp.views.store_order3, name='store_order3'),
    path('/order4', DeliveryApp.views.store_order4, name='store_order4'),
    
]
