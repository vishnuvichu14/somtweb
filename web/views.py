from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.views import auth_logout, auth_login


def landing_page(request):
    return render(request, 'web/landing_page.html')


def login_page(request):
    if request.POST:
        data = request.POST
        email = data['inputEmail']
        password = data['inputPassword']
        username = User.objects.get(email=email.lower()).username
        print(username)
        user = authenticate(request, username=str(username), password=str(password))
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard_page')
        else:
            print("invalid login")
    return render(request, 'web/login_page.html')


def logout_user(request):
    auth_logout(request)
    return redirect('landing_page')
