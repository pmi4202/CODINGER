from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Store, Menu, Order, DeliveryPrice, AppUser, DeliveryInfo, Option, Category, MenuSimple
from datetime import timedelta, datetime
from django.utils import timezone
from django.utils.timezone import utc

# Create your views here.

def store_login(request):
    if request.method == 'POST': # POST 방식으로 request를 통해 정보가 오면 
        # 변수(좌변이 변수이름)에 저장시켜 사용한다.
        username = request.POST['id']
        password = request.POST['password']
        # 로그인
        user = auth.authenticate(request, username=username, password=password)
        # 성공
        if user is not None:
            auth.login(request, user)
            return redirect('store_order')
        # 실패
        else:
            return render(request, 'store_login.html', {'error': 'id or password is incorrect.'})
    else:
        return render(request, 'store_login.html')
        
def store_logout(request):
    if request.method == 'POST': # POST 방식으로 request를 통해 정보가 오면
        # 로그아웃
        auth.logout(request)
        return redirect('store_order')
    return render(request, 'store_login.html')


#로그인 후, 처음 보이는 화면(디자인은 없음..)
def store_home(request):
    store = Store.objects.get(ownerName = request.user.username)
    return render(request, 'store_home.html', {'store':store})

#메뉴 관리 start
def store_menu(request):
    store = Store.objects.get(ownerName = request.user.username)
    menus = Menu.objects.filter(menuList = store).filter(menuOrder = 0)
    return render(request, 'store_menu.html', {'menus' : menus})

def store_menu_add(request):
    if request.method == 'POST':
        store = Store.objects.get(ownerName = request.user.username)

        menu = Menu()
        menu.menuList = store
        menu.categoryName = request.POST['menu_category']
        menu.menuName = request.POST['menu_name']
        menu.menuDetail = request.POST['menu_detail']
        menu.menuPrice = request.POST['menu_price']
        menu.menuOrder = 0
        menu.save()

        menus = Menu.objects.filter(menuList = store).filter(menuOrder = 0)
        return render(request, 'store_menu.html', {'menus':menus})
    else:
        store = Store.objects.get(ownerName = request.user.username)
        menus = Menu.objects.filter(menuList = store).filter(menuOrder = 0)
        return render(request, 'store_menu.html', {'menus':menus})

def store_menu_edit(request, menu_id):
    store = Store.objects.get(ownerName = request.user.username) #객체 전체 보여주기 용
    menus = Menu.objects.filter(menuList = store).filter(menuOrder = 0) #객체 전체 보여주기 용
    menu = get_object_or_404(Menu, pk= menu_id) # 특정 객체 가져오기(없으면 404 에러)
    return render(request, 'store_menu_edit.html', {'menu':menu, 'menus':menus})

def store_menu_update(request, menu_id):
    menu= get_object_or_404(Menu, pk= menu_id) # 특정 객체 가져오기(없으면 404 에러)
    menu.categoryName = request.GET['menu_category'] # 내용 채우기
    menu.menuName = request.GET['menu_name'] # 내용 채우기
    menu.menuPrice = request.GET['menu_price']
    menu.menuDetail = request.GET['menu_detail']
    menu.save()
    
    store = Store.objects.get(ownerName = request.user.username)
    menus = Menu.objects.filter(menuList = store).filter(menuOrder = 0)
    return render(request, 'store_menu.html', {'menus':menus})

def store_menu_delete(request, menu_id):
    menu= get_object_or_404(Menu, pk= menu_id) # 특정 객체 가져오기(없으면 404 에러)
    menu.delete()

    store = Store.objects.get(ownerName = request.user.username)
    menus = Menu.objects.filter(menuList = store).filter(menuOrder = 0)
    return render(request, 'store_menu.html', {'menus':menus})
#메뉴 관리 end

#분류관리 start
def store_category(request):
    store = Store.objects.get(ownerName = request.user.username)
    categories = Category.objects.filter(categoryList = store)
    return render(request, 'store_category.html', {'categories' : categories})

def store_category_add(request):
    if request.method == 'POST':
        store = Store.objects.get(ownerName = request.user.username)

        category = Category()
        category.categoryList = store
        category.categoryName = request.POST['category_name']
        category.orderMethod = request.POST['category_order_method']
        category.save()

        categories = Category.objects.filter(categoryList = store)
        return render(request, 'store_category.html', {'categories' : categories})
    else:
        return render(request, 'store_category_add.html')

def store_category_edit(request, category_id):
    store = Store.objects.get(ownerName = request.user.username) #객체 전체 보여주기 용
    categories = Category.objects.filter(categoryList = store) #객체 전체 보여주기 용
    category = get_object_or_404(Category, pk= category_id) # 특정 객체 가져오기(없으면 404 에러)
    return render(request, 'store_category_edit.html', {'category':category, 'categories':categories})

def store_category_update(request, category_id):
    category= get_object_or_404(Category, pk= category_id) # 특정 객체 가져오기(없으면 404 에러)
    store = Store.objects.get(ownerName = request.user.username)
    menus = Menu.objects.filter(menuList = store) # 해당 가게 메뉴 불러오기
    change_name = request.GET['category_name'] #변경 할 category이름

    for menu in menus:
        if menu.categoryName == category.categoryName :
            menu.categoryName = change_name
            menu.save()

    category.categoryName = change_name # 내용 채우기
    category.orderMethod = request.GET['category_order_method'] # 내용 채우기
    category.save()
    
    store = Store.objects.get(ownerName = request.user.username)
    categories = Category.objects.filter(categoryList = store)
    return render(request, 'store_category.html', {'categories':categories})

def store_category_delete(request, category_id):
    category= get_object_or_404(Category, pk= category_id) # 특정 객체 가져오기(없으면 404 에러)
    category.delete()

    store = Store.objects.get(ownerName = request.user.username)
    categories = Category.objects.filter(categoryList = store)
    return render(request, 'store_category.html', {'categories':categories})
#분류관리 end

#접수 대기
def store_order(request):
    orders = Order.objects.filter(storeId = request.user.username)
    wait_orders = orders.filter(status = "접수대기")
    order_menus = MenuSimple.objects.all()
    delivery_infos = DeliveryInfo.objects.all()
    return render(request, 'store_order.html', {'wait_orders':wait_orders, 'order_menus': order_menus, 'delivery_infos': delivery_infos})

#주문 정보
def store_order_detail(request, order_id):
    order= get_object_or_404(Order, pk= order_id)
    deliveryInfo = DeliveryInfo.objects.filter(deliveryInfoList = order)
    menu_simples = MenuSimple.objects.filter(orderId = order)
    #뒷 배경용 =>
    wait_orders = orders.filter(status = "접수대기")
    order_menus = MenuSimple.objects.all()
    delivery_infos = DeliveryInfo.objects.all()
    return render(request, 'store_order_detail.html', {'order':order, 'deliveryInfo':deliveryInfo, 'wait_orders':wait_orders, 'menu_simples':menu_simples, 'order_menus': order_menus, 'delivery_infos': delivery_infos})

#주문정보2
def store_order_detail2(request, order_id):
    order= get_object_or_404(Order, pk= order_id)
    deliveryInfo = DeliveryInfo.objects.filter(deliveryInfoList = order)
    menu_simples = MenuSimple.objects.filter(orderId = order)
    #뒷 배경용 =>
    orders = Order.objects.filter(storeId = request.user.username)
    proceed_orders = orders.filter(status = "진행중")
    order_menus = MenuSimple.objects.all()
    delivery_infos = DeliveryInfo.objects.all()
    return render(request, 'store_order_detail2.html', {'order':order, 'deliveryInfo':deliveryInfo, 'proceed_orders':proceed_orders, 'menu_simples':menu_simples, 'order_menus': order_menus, 'delivery_infos': delivery_infos})

#주문 접수
def store_order_add(request, order_id):
    if request.method == 'POST':
        order= get_object_or_404(Order, pk= order_id)
        order.status = "진행중"
        time = int(request.POST['time'])
        #new
        #배달 예상 시간
        today = datetime.now()
        if today.minute + time >= 60:
            if today.hour +1 >=24:
                today = today.replace(date = today.date + 1)
                today = today.replace(hour = 0)
            else:
                today = today.replace(hour = today.hour +1)

            today = today.replace(minute = today.minute + time-60)
        else :
            today = today.replace(minute = today.minute + time)

        order.deliveryEndTime = order.deliveryEndTime.replace(hour = today.hour, minute = today.minute, second= today.second)

        #Duration 시간
        order.deliveryTime = order.deliveryTime.replace(hour = int(time/60), minute = int(time%60), second =0)
        #
        order.save()
        #store_order.html에 필요한 자료=>#
        orders = Order.objects.filter(storeId = request.user.username)
        wait_orders = orders.filter(status = "접수대기")
        order_menus = MenuSimple.objects.all()
        #
        return render(request, 'store_order.html', {'wait_orders':wait_orders, 'order_menus': order_menus})
    else:
        return render(request, 'store_order_add.html')
#주문 취소
def store_order_delete(request, order_id):
    order= get_object_or_404(Order, pk= order_id)
    order.status = "취소"
    order.save()

    orders = Order.objects.filter(storeId = request.user.username).filter(status = "취소")

    return render(request, 'store_order_delete.html', {'orders':orders})

#진행중
def store_order2(request):
    orders = Order.objects.filter(storeId = request.user.username)
    proceed_orders = orders.filter(status = "진행중")
    for order in proceed_orders:
        #Duration 시간
        today = datetime.now()
        #초
        if order.deliveryEndTime.second - today.second < 0: #현재 남은 초
            if order.deliveryEndTime.minute - today.minute > 0: #현재 남은 분
                order.deliveryTime = order.deliveryTime.replace(second = order.deliveryEndTime.second - today.second + 60)
                #분
                order.deliveryTime = order.deliveryTime.replace(minute = order.deliveryEndTime.minute - today.minute-1)
            else :
                if order.deliveryEndTime.hour - today.hour > 0: #현재 남은 시간
                    order.deliveryTime = order.deliveryTime.replace(hour = order.deliveryEndTime.hour - today.hour -1)
                    order.deliveryTime = order.deliveryTime.replace(minute = order.deliveryEndTime.minute - today.minute-1+60)
                    order.deliveryTime = order.deliveryTime.replace(second = order.deliveryEndTime.second - today.second + 60)
                else:
                    order.deliveryTime = order.deliveryTime.replace(second = 0)
        else :
            if order.deliveryEndTime.hour - today.hour > 0 or order.deliveryEndTime.minute - today.minute > 0 :
                order.deliveryTime = order.deliveryTime.replace(second = order.deliveryEndTime.second - today.second)

        order.save()

    menu_simples2 = MenuSimple.objects.all()
    delivery_infos = DeliveryInfo.objects.all()

    return render(request, 'store_order2.html', {'proceed_orders':proceed_orders, 'menu_simples2': menu_simples2, 'delivery_infos': delivery_infos})

#완료내역
def store_order3(request):
    return render(request, 'store_order3.html')

#취소내역
def store_order4(request):
    return render(request, 'store_order4.html')