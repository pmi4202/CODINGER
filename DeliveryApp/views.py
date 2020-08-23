from django.shortcuts import render

# Create your views here.

def store_login(request):
    return render(request, 'store_login.html')

#로그인 후, 처음 보이는 화면(디자인은 없음..)
def store_home(request):
    return render(request, 'store_home.html')

#메뉴 관리
def store_menu(request):
    return render(request, 'store_menu.html')

#접수 대기
def store_order(request):
    return render(request, 'store_order.html')
#주문 정보
def store_order_detail(request):
    return render(request, 'store_order_detail.html')
#주문 접수
def store_order_add(request):
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