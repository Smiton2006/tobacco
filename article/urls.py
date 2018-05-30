
from django.conf.urls import url
from django.contrib import admin

import views

urlpatterns = [
    url(r'^articles_all/all$', views.articles),
    url(r'^article/get/(?P<article_id>\d+)$', views.article),
    url(r'^article/addlike/(?P<article_id>\d+)$', views.addlike),
    url(r'^article/addcoment/(?P<article_id>\d+)$', views.addcoment),
    url(r'^article/add$', views.addarticle),
    url(r'^page/(\d+)$', views.articles), 
    url(r'^', views.articles),    
]
