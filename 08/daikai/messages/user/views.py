from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from . import models

# Create your views here.

def require_login(request):
    return render(request, 'user/login.html')

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    #print(username, password)
    rt = models.validate_login(username, models.strmd5(password))
    if rt:
        request.session['user'] = rt
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {'error' : '用户名或密码错误', 'username' : username, 'password' : password}
        return render(request, 'user/login.html', context)

def list_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    users = models.get_users()
    return render(request, 'user/list.html', {'users' : users})

def delete_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    _id = request.GET.get('id', '')
    models.delete_user(_id)
    return HttpResponseRedirect('/user/list_user/')

def logout(request):
     request.session.flush()
     return HttpResponseRedirect('/user/require_login/')

def create_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    return render(request, 'user/create.html')

def save_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')

    rt, error = models.validate_add_user(username, age, tel, password)
    if rt:
        #验证成功
        models.add_user(username, age, tel, models.strmd5(password))
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {}
        context['error'] = error
        context['username'] = username
        context['password'] = password
        context['age'] = age
        context['tel'] = tel
        return render(request, 'user/create.html', context)

def view_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    uid = request.GET.get('id', '')
    user = models.get_user_by_id(uid)
    return render(request, 'user/view.html', user)

def modify_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    id = request.POST.get('id', '')
    username = request.POST.get('username', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')

    rt, error = models.validate_modify_user(username, age, tel)
    if rt:
        #验证成功
        models.modify_user(username, age, tel)
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {}
        context['error'] = error
        context['username'] = username
        #context['password'] = password
        context['age'] = age
        context['tel'] = tel
        return render(request, 'user/view.html', context)

def view_password(request):
     if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
     uid = request.GET.get('id','')
     user = models.get_user_by_id(uid)
     return render(request, 'user/password.html', user)

def modify_password(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    old_password = request.POST.get('old_password','')
    new_password = request.POST.get('new_password','')
    uid = request.POST.get('id', '')
    user = models.get_user_by_id(uid)
   
    if models.strmd5(old_password) == user['password']:
        rt, error = models.validate_modify_password(new_password)
        if rt:
            models.modify_password(uid, models.strmd5(new_password)) 
            return HttpResponseRedirect('/user/list_user/')
        else:
            context = {'error': error, 'username': user['username'], 'id': user['id']}
            return render(request, 'user/password.html', context)
    else:
        context = {'error': '旧密码不正确', 'username': user['username'], 'id': user['id']}        
        return render(request, 'user/password.html', context)
     