from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    # return HttpResponse('He   llo Django')
    return render(request, 'index.html')


# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        # if username == 'admin' and password == 'admin123':
        if user is not None:
            auth.login(request, user)  # 登录
            # return HttpResponse('login success')
            # return HttpResponseRedirect('/even_manage')
            response = HttpResponseRedirect('/even_manage')
            # response.set_cookie('user', username, 3600)
            request.session['user'] = username
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})


@login_required
def even_manage(request):
    # return render(request, 'even_manage.html')
    # username = request.COOKIES.get('user', '')
    username = request.session.get('user', '')
    return render(request, 'even_manage.html', {'user': username})
