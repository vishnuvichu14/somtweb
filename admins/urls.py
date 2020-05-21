from django.urls import path
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.views import auth_logout, auth_login
from .views import dashboard_page

urlpatterns = [
    path("", dashboard_page, name="dashboard_page"),
]
