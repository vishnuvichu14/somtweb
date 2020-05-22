from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def dashboard_page(request):
    return render(request, 'admins/dashboard_page.html')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def farms_detail_page(request):
    return render(request, 'admins/farms_details_page.html')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def cows_detail_page(request):
    return render(request, 'admins/cows_details_page.html')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def customers_detail_page(request):
    return render(request, 'admins/customers_details_page.html')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def carriers_detail_page(request):
    return render(request, 'admins/carriers_details_page.html')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def transaction_detail_page(request):
    return render(request, 'admins/transaction_details_page.html')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def order_detail_page(request):
    return render(request, 'admins/orders_details_page.html')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def notification_page(request):
    return render(request, 'admins/notification_page.html')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def send_message_page(request):
    return render(request, 'admins/send_message_page.html')
