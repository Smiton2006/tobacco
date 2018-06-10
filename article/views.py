# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, render_to_response,redirect
from django.template.loader import get_template
from article.models import Article, Comments
from django.contrib.auth.models import User
from forms import CommentForm,ArticleForm
from django.template.context_processors import csrf
from django.contrib import auth
import time
from django.core.paginator import Paginator


now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# Create your views here.
def articles(request,page_number=1):
    all_articles = Article.objects.all()
    paginator = Paginator(all_articles, 3)
    page = paginator.page(page_number)
    args = {}
    args['articles'] = page
    args['username'] = auth.get_user(request).username
    args['pages'] = paginator.page_range
    return render_to_response('articles.html', args)

def article(request, article_id=1):
    coment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id = article_id)
    args['comments'] = Comments.objects.filter(comments_article=article_id)
    args['form'] = coment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)

def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            return redirect('/')
        else:
            article = Article.objects.get(id = article_id)
            article.article_likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(article_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def addcoment(request, article_id):
    if request.POST and 'pause' not in request.session:
        form  = CommentForm(request.POST)   
        if form.is_valid():
            comment = form.save(commit = False)
            comment.comments_article = Article.objects.get(id = article_id)
            comment.comments_date = now_time
            user_id = auth.get_user(request).id
            comment.comments_user = User.objects.get(id = user_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    url =  request.META.get('HTTP_REFERER')
    return redirect(url)

def addarticle(request):
    form  = ArticleForm
    args = {}
    args.update(csrf(request)) 
    args['form'] = form
    args['username'] = auth.get_user(request).username
    if request.POST:
        form  = ArticleForm(request.POST)   
        if form.is_valid():
            article = form.save(commit = False)
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            article.article_date = now_time            
            form.save()
            return redirect('/')
    return render_to_response('add_article.html', args)