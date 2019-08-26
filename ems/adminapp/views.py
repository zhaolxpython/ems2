import random
import string

from django.db import transaction
from django.shortcuts import render, HttpResponse, redirect
from adminapp.models import User
from adminapp.captcha.image import ImageCaptcha


def login(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    if username:
        username = username.encode('latin-1').decode('utf-8')
    result = User.objects.filter(username=username, password=password)
    if result:
        request.session['login'] = 1
        return redirect('employee:employee')
    return render(request, 'adminapp/login.html')


def loginlogic(request):
    try:
        with transaction.atomic():
            username = request.GET.get('username')
            password = request.GET.get('password')
            remember = request.GET.get('remember')
            result = User.objects.filter(username=username, password=password)
            if result:
                res = HttpResponse('1')
                request.session['login'] = 1
                if remember == '1':
                    res.set_cookie('username', username.encode('utf-8').decode('latin-1'), max_age=3*24*60*60)
                    res.set_cookie('password', password, max_age=3*24*60*60)
                return res
            return HttpResponse('0')
    except:
        return HttpResponse('0')


def regist(request):
    return render(request, 'adminapp/regist.html')


def registlogic(request):
    try:
        username = request.GET.get('username')
        name = request.GET.get('name')
        password = request.GET.get('password')
        gender = int(request.GET.get('gender'))
        result = User.objects.create(username=username, name=name, password=password, gender=gender)
        if result:
            return HttpResponse('1')
        else:
            return HttpResponse('0')
    except:
        return HttpResponse('0')


def getcaptche(request):
    image = ImageCaptcha()
    code = random.sample(string.ascii_letters + string.digits, 4)
    random_code = ''.join(code)
    print(random_code)
    request.session['code'] = random_code
    data = image.generate(random_code)
    return HttpResponse(data, 'image/png')


def checkname(request):
    username = request.GET.get('username')
    result = User.objects.filter(username=username)
    if result:
        return HttpResponse('0')
    else:
        return HttpResponse('1')


def checkcaptcha(request):
    capt = request.GET.get('captcha')
    code = request.session.get('code')
    if code.lower() == capt.lower():
        return HttpResponse('1')
    else:
        return HttpResponse('0')


def checkcaptcha1(request):
    capt = request.GET.get('captcha')
    code = request.session.get('code')
    if code.lower() == capt.lower():
        return HttpResponse('1')
    else:
        return HttpResponse('0')
