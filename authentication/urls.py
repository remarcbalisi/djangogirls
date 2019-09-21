from django.urls import path
from . import views

urlpatterns = [
    path('user/login', views.signin, name='user_login'),
]
