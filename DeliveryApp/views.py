from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

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
            return redirect('store_home')
        # 실패
        else:
            return render(request, 'store_login.html', {'error': 'id or password is incorrect.'})
    else:
        return render(request, 'store_login.html')
        
def store_logout(request):
    if request.method == 'POST': # POST 방식으로 request를 통해 정보가 오면
        # 로그아웃
        auth.logout(request)
        return redirect('store_home')
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