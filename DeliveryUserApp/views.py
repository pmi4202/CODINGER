from django.shortcuts import render

# Create your views here.
#앱 로그인
def user_login(request):
    return render(request, 'user_login.html')
#앱 회원가입
def user_signup(request):
    return render(request, 'user_signup.html')
#앱 메인
def user_home(request):
    return render(request, 'user_home.html')
#앱 카테고리 리스트
def user_category_list(request):
    return render(request, 'user_category_list.html')
#앱 마이페이지
def user_detail(request):
    return render(request, 'user_detail.html')
#앱 지도페이지
def user_map(request):
    return render(request, 'user_map.html')
#앱 가게 정보
def user_store_detail(request):
    return render(request, 'user_store_detail.html')
#장바구니
def user_order_detail(request):
    return render(request, 'user_order_detail.html')
#주문담기
def user_order_add(request):
    return render(request, 'user_order_add.html')