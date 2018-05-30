from django.conf.urls import url

from . import views

urlpatterns = [
     
    url(r'^get/(?P<tobacco_id>\d+)$', views.tobacco),
    url(r'^add$', views.tobacco_add), 
    url(r'^', views.tobacco_list),
]