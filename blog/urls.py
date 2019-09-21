from django.urls import path
from . import views

from django.conf.urls import url

urlpatterns = [
    path('', views.post_list, name='post_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.post_edit, name='post_edit'),
    path('post/new', views.post_new, name='post_new'),
]