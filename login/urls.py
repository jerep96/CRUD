from django.conf.urls import include, url
from django.contrib import admin

from login import views

urlpatterns = [
    url('login/', views.login, name='login')
]
