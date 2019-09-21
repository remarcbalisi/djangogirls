from django.urls import path
from . import views

from django.conf.urls import url

urlpatterns = [
    path('', views.post_list, name='post_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]