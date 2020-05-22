from uuid import uuid1

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.views import auth_logout, auth_login
from django.contrib.auth.decorators import user_passes_test, login_required

from payment.models import Order, Transaction


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
            if user.groups.filter(name='Customer').exists():
                return redirect('order_payment_page')
            elif user.groups.filter(name='Admin').exists():
                return redirect('dashboard_page')
        else:
            print("invalid login")
    return render(request, 'web/login_page.html')


def logout_user(request):
    auth_logout(request)
    return redirect('landing_page')


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Customer').exists())
def order_payment_page(request):
    orders = Order.objects.filter(customer_id=request.user.id)
    if request.POST:
        data = request.POST
        order_id = int(data.get('order_id'))
        order = Order.objects.get(id=order_id)
        txnid = str(uuid1().int >> 64)
        transaction = Transaction.objects.create(amount=float(order.amount), payment_mode=Transaction.PAYUBIZ,
                                                 txnid=txnid,
                                                 customer=request.user, order=order, status=Transaction.INITIATED)
        request.session["transaction_id"] = txnid
        return redirect("payubiz_entrance")
    return render(request, 'web/order_payment_page.html', {'orders': orders})
