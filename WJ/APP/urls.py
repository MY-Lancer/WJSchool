"""WJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from .views import *

urlpatterns = [
    #默认页面
    path('',IndexView.as_view(),name='index'),
    #注册页面的路由
    path('register/',RegisterView.as_view(),name='register'),    
    #图片验证码的路由 
    path('imagecode/', ImageCodeView.as_view(),name='imagecode'),
]

