from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_page(request):
    return render(request, 'admins/dashboard_page.html')

