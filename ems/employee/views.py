import os
import uuid
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from employee.models import Employee


def employee(request):
    def emp_default(e):
        if isinstance(e, Employee):
            return {'id': e.id, 'name': e.name, 'age': e.age, 'salary': str(e.salary),
                    'headpic': e.headpic.url}
    users = list(Employee.objects.all())
    return JsonResponse({'users': users}, json_dumps_params={'default': emp_default})


# def employee(request):
#     number = request.GET.get('num', 1)
#     pagtor = Paginator(Employee.objects.all(), per_page=3)
#     page = pagtor.page(number)
#     return render(request, 'employee/emplist.html', {
#         'page': page, 'num': number
#     })


def addemp(request):
    return render(request, 'employee/addEmp.html')


def addemplogic(request):
    try:
        name = request.POST.get('name')
        if name == '' or name == None:
            return HttpResponse('2')
        salary = request.POST.get('salary')
        age = request.POST.get('age')
        file = request.FILES.get('file')
        if file:
            file.name = str(uuid.uuid4()) + os.path.splitext(file.name)[0]
        Employee.objects.create(name=name, salary=salary, age=age, headpic=file)
        return HttpResponse('1')
    except:
        return HttpResponse('2')


# def addemplogic(request):
#     name = request.POST.get('name')
#     salary = request.POST.get('salary')
#     age = request.POST.get('age')
#     file = request.FILES.get('file')
#     if file:
#         file.name = str(uuid.uuid4()) + os.path.splitext(file.name)[0]
#     Employee.objects.create(name=name, salary=salary,
#                             age=age, headpic=file)
#     pagtor = Paginator(Employee.objects.all(), per_page=3)
#     page_nums = pagtor.num_pages
#     return redirect(reverse('employee:employee') + '?num=' + str(page_nums))


# def updateemp(request):
#     id1 = request.GET.get('id')
#     page_num1 = request.GET.get('pagenum1')
#     request.session['page_num1'] = page_num1
#     user = Employee.objects.filter(id=id1)[0]
#     return render(request, 'employee/updateEmp.html', {
#         'user': user
#     })

def updateemp(request):
    id1 = request.GET.get('id')
    request.session['id1'] = id1
    return HttpResponse('1')


def updatelogic(request):
    def emp_default(e):
        if isinstance(e, Employee):
            return {'id': e.id, 'name': e.name, 'age': e.age, 'salary': str(e.salary),
                    'headpic': e.headpic.url}
    id1 = request.session.get('id1')
    user = list(Employee.objects.filter(id=id1))
    return JsonResponse({'user': user}, json_dumps_params={'default': emp_default},)


def update(request):
    id1 = request.session.get('id1')
    user = Employee.objects.get(pk=id1)
    user.name = request.POST.get('name')
    user.salary = request.POST.get('salary')
    user.age = request.POST.get('age')
    file = request.FILES.get('file')
    if file:
        file.name = str(uuid.uuid4()) + os.path.splitext(file.name)[0]
        user.headpic = file
    user.save()
    return HttpResponse('1')




# def updatelogic(request):
#     def emp_default(e):
#         if isinstance(e, Employee):
#             return {'id': e.id, 'name': e.name, 'age': e.age, 'salary': str(e.salary),
#                     'headpic': e.headpic.url}
#     id1 = request.session.get('id1')
#     user = list(Employee.objects.filter(id=id1)[0])
#     user.name = request.POST.get('name')
#     user.age = request.POST.get('age')
#     user.salary = request.POST.get('salary')
#     file = request.FILES.get('file')
#     if file:
#         file.name = str(uuid.uuid4()) + os.path.splitext(file.name)[0]
#         user.headpic = file
#     user.save()
#     return redirect(reverse('employee:employee') + '?num=' + page_num1)


def delemp(request):
    # with transaction.atomic():
    id2 = request.GET.get('id')
    print(id2)
    # page_num2 = request.GET.get('pagenum2')
    user = Employee.objects.get(id=id2)
    user.delete()
    return HttpResponse('1')


# def delemp(request):
#     id2 = request.GET.get('id')
#     page_num2 = request.GET.get('pagenum2')
#     page = Paginator(Employee.objects.all(), per_page=3)
#     pages = page.count
#     user = Employee.objects.get(id=id2)
#     user.delete()
#     if pages % 3 == 1:
#         page_num2 = str(int(page_num2) - 1)
#     return redirect(reverse('employee:employee') + '?num=' + page_num2)


# def checkname(request):
#     name = request.POST.get('name')
#     result = Employee.objects.filter(name=name)
#     if result:
#         return HttpResponse('0')
#     else:
#         return HttpResponse('1')