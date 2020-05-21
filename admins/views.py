from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_page(request):
    return render(request, 'admins/dashboard_page.html')


@login_required
def farms_detail_page(request):
    return render(request, 'admins/farms_details_page.html')


@login_required
def cows_detail_page(request):
    return render(request, 'admins/cows_details_page.html')


@login_required
def customers_detail_page(request):
    return render(request, 'admins/customers_details_page.html')


@login_required
def carriers_detail_page(request):
    return render(request, 'admins/carriers_details_page.html')


@login_required
def transaction_detail_page(request):
    return render(request, 'admins/transaction_details_page.html')


@login_required
def order_detail_page(request):
    return render(request, 'admins/orders_details_page.html')


@login_required
def notification_page(request):
    return render(request, 'admins/notification_page.html')

@login_required
def send_message_page(request):
    return render(request, 'admins/send_message_page.html')