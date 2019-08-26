# encoding: utf-8
from django.urls import path
from adminapp import views

app_name = 'adminapp'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('loginlogic/', views.loginlogic, name='loginlogic'),
    path('regist/', views.regist, name='regist'),
    path('registlogic/', views.registlogic, name='registlogic'),
    path('getcaptche/', views.getcaptche, name='getcaptche'),
    path('checkname/', views.checkname, name='checkname'),
    path('checkcaptcha/', views.checkcaptcha, name='checkcaptcha'),
    path('checkcaptcha1/', views.checkcaptcha1, name='checkcaptcha1'),
]
