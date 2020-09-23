from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Store, Menu, Order, DeliveryPrice, User, DeliveryInfo, Option, Category

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

#메뉴 관리
def store_menu(request):
    store = Store.objects.get(ownerName = request.user.username)
    menus = Menu.objects.filter(menuList = store)
    return render(request, 'store_menu.html', {'menus' : menus})

#메뉴추가
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

        menus = Menu.objects.filter(menuList = store)
        return render(request, 'store_menu.html', {'menus':menus})
    else:
        store = Store.objects.get(ownerName = request.user.username)
        menus = Menu.objects.filter(menuList = store)
        return render(request, 'store_menu.html', {'menus':menus})

def store_menu_edit(request, menu_id):
    menu = get_object_or_404(Menu, pk= menu_id) # 특정 객체 가져오기(없으면 404 에러)
    return render(request, 'store_menu_edit.html', {'menu':menu})

def store_menu_update(request, menu_id):
    menu= get_object_or_404(Menu, pk= menu_id) # 특정 객체 가져오기(없으면 404 에러)
    menu.categoryName = request.GET['categoryName'] # 내용 채우기
    menu.menuName = request.GET['menuName'] # 내용 채우기
    menu.menuPrice = request.GET['menuPrice']
    menu.menuDetail = request.GET['menuDetail']
    menu.save()
    
    store = Store.objects.get(ownerName = request.user.username)
    menus = Menu.objects.filter(menuList = store)
    return render(request, 'store_menu.html', {'menus':menus})

def store_menu_delete(request, menu_id):
    menu= get_object_or_404(Menu, pk= menu_id) # 특정 객체 가져오기(없으면 404 에러)
    menu.delete()

    store = Store.objects.get(ownerName = request.user.username)
    menus = Menu.objects.filter(menuList = store)
    return render(request, 'store_menu.html', {'menus':menus})

#분류관리
def store_category(request):
    store = Store.objects.get(ownerName = request.user.username)
    categories = Category.objects.filter(categoryList = store)
    return render(request, 'store_category.html', {'categories' : categories})

#분류추가
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

#접수 대기
def store_order(request):
    orders = Order.objects.filter(storeId = request.user.username)
    wait_orders = orders.filter(status = "접수대기")
    
    return render(request, 'store_order.html', {'wait_orders':wait_orders})

#주문 정보
def store_order_detail(request):
    return render(request, 'store_order_detail.html')
#주문 접수
def store_order_add(request):
    if request.method == 'POST':
        time=request.POST['time']
        return render(request, 'store_order.html', {'time':'time'})
    else:
        return render(request, 'store_order_add.html')
#주문 취소
def store_order_delete(request):
    return render(request, 'store_order_delete.html')

#진행중
def store_order2(request):
    return render(request, 'store_order2.html')

#완료내역
def store_order3(request):
    return render(request, 'store_order3.html')

#취소내역
def store_order4(request):
    return render(request, 'store_order4.html')