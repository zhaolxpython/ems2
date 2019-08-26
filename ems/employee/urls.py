# encoding: utf-8
from django.urls import path
from employee import views
app_name = 'employee'
urlpatterns = [
    path('employee/', views.employee, name='employee'),
    path('addemp/', views.addemp, name='addemp'),
    path('addemplogic/', views.addemplogic, name='addemplogic'),
    path('updateemp/', views.updateemp, name='updateemp'),
    path('updatelogic/', views.updatelogic, name='updatelogic'),
    path('update/', views.update, name='update'),
    path('delemp/', views.delemp, name='delemp'),
    # path('checkname/', views.checkname, name='checkname'),

]
