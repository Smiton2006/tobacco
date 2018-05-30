# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response,redirect
from django.template.loader import get_template
from tobacco.models import Tobacco,Tobacco_rating
from django.template.context_processors import csrf
from django.contrib import auth
from forms import TobaccoForm
from django.db.models import Avg
# Create your views here.

def tobacco_list(request):
    args = {}
    args['tobaccos'] = Tobacco.objects.annotate(avg_rate = Avg('tobacco_rating__rating'))
    args['username'] = auth.get_user(request).username
    return render_to_response('tobacco_list.html',args)

def tobacco(request, tobacco_id):
    args = {}
    args.update(csrf(request)) 
    args['tobacco'] = Tobacco.objects.get(id = tobacco_id)
    args['username'] = auth.get_user(request).username
    if request.POST:
        try:
            tobacco_rating = Tobacco_rating.objects.get(tobacco_id_id = tobacco_id, user_id_id = auth.get_user(request).id)
            tobacco_rating.rating = request.POST['rate']
            #tobacco_rating.save()
        except Tobacco_rating.DoesNotExist:
            new_values = {'tobacco_id_id': tobacco_id, 'user_id_id': auth.get_user(request).id, 'rating':request.POST['rate'] }
            tobacco_rating = Tobacco_rating(**new_values)
        tobacco_rating.save()
        return redirect('/tobacco/')
    return render_to_response('tobacco.html',args)

def tobacco_add(request):
    form  = TobaccoForm
    args = {}
    args.update(csrf(request)) 
    args['form'] = form
    args['username'] = auth.get_user(request).username
    if request.POST:
        form  = TobaccoForm(request.POST) 
        print  form 
        if form.is_valid():           
            form.save()
            return redirect('/tobacco')
    return render_to_response('tobacco_add.html', args)    