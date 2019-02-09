from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'login'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login/final_login.html'), name='login'),
    path('tmp/', views.Signin, name='login'),
    path('signup_for_test/', views.Signup, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.Main, name='main'),
    path('', views.Main),
    path('mypage/', views.MyPage, name='mypage'),
    path('lendunbrella/', views.LendUnbrella, name='lendunbrella'),
]