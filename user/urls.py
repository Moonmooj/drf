"""ai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from user import views

urlpatterns = [
    # user/
    path('', views.UserView.as_view()), # CBV는 as_view() 를 적어주어야함
    path('login/', views.UserAPIView.as_view()),
    path('logout/', views.UserAPIView.as_view()),
    path('<obj_id>/', views.UserView.as_view())
]
