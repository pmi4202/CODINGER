from django.shortcuts import render, redirect, get_object_or_404
from DeliveryApp.models import Store, Menu, Order, DeliveryPrice, User, DeliveryInfo, Option, Category

# Create your views here.
#앱 로그인
def user_login(request):
  if request.method == 'POST': # POST 방식으로 request를 통해 정보가 오면 
      # 변수(좌변이 변수이름)에 저장시켜 사용한다.
      username = request.POST['id']
      password = request.POST['password']
      # 로그인
      users = User.objects.filter(userName= username)
      if users:
        user = auth.authenticate(request, username=username, password=password)

      # 성공
      if user is not None:
          auth.login(request, user)
          return redirect('store_order')
      # 실패
      else:
          return render(request, 'user_login.html', {'error': 'id or password is incorrect.'})
  else:
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
  store = Store.objects.get(ownerName = "hello")#임시로 지정
  menus = Menu.objects.filter(menuList = store)
  #menu = get_object_or_404(Menu, pk= menu_id)
  categories = Category.objects.filter(categoryList = store)
  return render(request, 'user_store_detail.html', {'menus':menus, 'categories':categories})

#장바구니
def user_order_detail(request):
  return render(request, 'user_order_detail.html')
#주문담기
def user_order_add(request, menu_id):
    menu = get_object_or_404(Menu, pk = menu_id) # 특정 객체 가져오기(없으면 404 에러)
    #menu_order = menu

    menu_order = Menu() #새로운 객체 생성
    menu_order.menuList = menu.menuList
    menu_order.categoryName = menu.categoryName
    menu_order.menuName = menu.menuName
    menu_order.menuDetail = menu.menuDetail
    menu_order.menuPrice = menu.menuPrice
    menu_order.menuOrderPrice = menu.menuPrice
    menu_order.menuOrder = menu.menuOrder+1
    menu_order.save()

    return render(request, 'user_order_add.html', {'menu_order':menu_order})

#메뉴 MINUS
def user_menu_minus(request, menu_id):
    menu_order = get_object_or_404(Menu, pk = menu_id)
    if menu_order.menuOrder > 1 :
        menu_order.menuOrder = menu_order.menuOrder -1
        menu_order.menuOrderPrice = menu_order.menuOrder * menu_order.menuPrice
    menu_order.save()
    return render(request, 'user_order_add.html', {'menu_order':menu_order})

#메뉴 PLUS
def user_menu_plus(request, menu_id):
    menu_order = get_object_or_404(Menu, pk = menu_id)

    menu_order.menuOrder = menu_order.menuOrder +1
    menu_order.menuOrderPrice = menu_order.menuOrder * menu_order.menuPrice
    menu_order.save()
    return render(request, 'user_order_add.html', {'menu_order':menu_order})

#뒤로 가기 누르면 객체 없애기.. 