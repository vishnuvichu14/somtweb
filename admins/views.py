from django.shortcuts import render


def dashboard_page(request):
    return render(request,'admins/dashboard_page.html')
