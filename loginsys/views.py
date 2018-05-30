# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response,redirect
from django.template.context_processors import csrf
from django.contrib import auth

# Create your views here.

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error']  = 'Пользователь или пароль неверный'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    url =  request.META.get('HTTP_REFERER')
    return redirect (url)

def register(request):
    args = {}
    args.update(csrf(request))
    form = auth.forms.UserCreationForm()
    print type(form)
    for line in form:
        print line
    args['form'] = form
    if request.POST:
        newuser_form = auth.forms.UserCreationForm(request.POST)
        if newuser_form.is_valid():
            #запоминаем данные для логина пользователя после регистрации
            user = newuser_form.save()
            password = newuser_form.clean_password2()
            newuser = auth.authenticate(username = user, password = password )
            auth.login (request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)  