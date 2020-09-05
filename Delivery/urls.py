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
import DeliveryUserApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DeliveryApp.views.store_login, name='store_login'),
    path('logout/', DeliveryApp.views.store_logout, name='store_logout'),
    path('home/', DeliveryApp.views.store_home, name='store_home'),
    path('menu/', DeliveryApp.views.store_menu, name='store_menu'),
    path('order/', DeliveryApp.views.store_order, name='store_order'),
    path('order/detail/', DeliveryApp.views.store_order_detail, name='store_order_detail'),
    path('order/add/', DeliveryApp.views.store_order_add, name='store_order_add'),
    path('order/delete/', DeliveryApp.views.store_order_delete, name='store_order_delete'),
    path('order2/', DeliveryApp.views.store_order2, name='store_order2'),
    path('order3/', DeliveryApp.views.store_order3, name='store_order3'),
    path('order4/', DeliveryApp.views.store_order4, name='store_order4'),
    path('app/', DeliveryUserApp.views.user_home, name='user_home'),
    path('app/login/', DeliveryUserApp.views.user_login, name='user_login'),
    path('app/signup/', DeliveryUserApp.views.user_signup, name='user_signup'),
    path('app/detail/', DeliveryUserApp.views.user_detail, name='user_detail'),
    path('app/categories/1/', DeliveryUserApp.views.user_category_list, name='user_category_list'),
    path('app/map/', DeliveryUserApp.views.user_map, name='user_map'),
    path('app/stores/1/', DeliveryUserApp.views.user_store_detail, name='user_store_detail'),
    path('app/order/detail/', DeliveryUserApp.views.user_order_detail, name='user_order_detail'),
    path('app/order/add/', DeliveryUserApp.views.user_order_add, name='user_order_add'),
]
