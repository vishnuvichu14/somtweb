from __future__ import unicode_literals
import requests
from django.contrib.auth.models import User
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from payment.util import generate_hash, verify_hash
from .models import Transaction, Order
from django.contrib import messages
from django.conf import settings
import os


def payment_payubiz(request):
    if request.method == "POST" or "GET":
        txnid = request.session.get("transaction_id")
        transaction = Transaction.objects.get(txnid=txnid)
        title = "Milk Payment"
        amount = int(transaction.amount)
        user = User.objects.get(id=transaction.customer.id)
        mkey = settings.PAYU_INFO['merchant_key']
        surl = request.build_absolute_uri(reverse('succ_paybiz'))
        curl = request.build_absolute_uri(reverse('cancel_payubiz'))
        furl = request.build_absolute_uri(reverse('failure_payubiz'))
        data = dict(key=mkey, txnid=txnid, amount=amount, product_info=title, first_name=user.username,
                    email=user.email,
                    phone=user.profile.phone)
        hash = generate_hash(data)
        data.update({'hash': hash, 'surl': surl, 'curl': curl, 'furl': furl})
        return render(request, 'payment/pay_redirect.html', {'form': data, 'IS_PRODUCTION': settings.IS_PRODUCTION})
    else:
        raise SuspiciousOperation("Invalid request")


def key_collect_payubiz(request):
    data = {'key': request.POST.get('key'), 'txnid': request.POST.get('txnid'), 'amount': request.POST.get('amount'),
            'product_info': request.POST.get('product_info'), 'first_name': request.POST.get('first_name'),
            'email': request.POST.get('email'), 'hash': request.POST.get('hash'), 'status': request.POST.get('status')}
    try:
        data.update({'additionalCharges': request.POST.get('additionalCharges')})
    except:
        pass
    return data


@csrf_exempt
def succ_payubiz(request):
    msg = ""
    if request.method == "POST":
        data = key_collect_payubiz(request)
        if verify_hash(data):
            trns = Transaction.objects.get(txnid=data['txnid'])
            trns.payment_id = request.POST.get('payuMoneyId')
            trns.payu_status = (request.POST.get('status') == 'success')  # Boolean
            trns.status = Transaction.PAID
            trns.error_code = request.POST.get('error')  # should return no_error e000
            trns.error_message = request.POST.get('error_Message')
            trns.bank_refnum = request.POST.get('bank_ref_num')
            trns.mihpay_id = request.POST.get('mihpayid')
            trns.payment_added_on = request.POST.get('addedon')
            trns.payment_mode = request.POST.get('mode')
            trns.additional_charges = data.get("additionalCharges", 0)
            trns.field9 = request.POST.get('field9')
            trns.pg_type = request.POST.get('PG_TYPE')
            trns.save()
            order = Order.objects.get(id=trns.order.id)
            order.is_paid = True
            order.save()
            msg = "Payment Success"
    else:
        raise SuspiciousOperation("Invalid access")
    messages.success(request, msg)
    return redirect('paysuccess')


@csrf_exempt
def failure_payubiz(request):
    if request.method == "POST" or "GET":
        data = key_collect_payubiz(request)
        if verify_hash(data):
            trns = Transaction.objects.get(txnid=data['txnid'])
            trns.payment_id = request.POST.get('payuMoneyId')
            trns.payu_status = (request.POST.get('status') == 'success')  # Boolean
            trns.status = Transaction.FAILED
            trns.error_code = request.POST.get('error')  # should return no_error e000
            trns.error_message = request.POST.get('error_Message')
            trns.bank_refnum = request.POST.get('bank_ref_num')
            trns.mihpay_id = request.POST.get('mihpayid')
            trns.payment_added_on = request.POST.get('addedon')
            trns.pg_type = request.POST.get('PG_TYPE')
            trns.payment_mode = request.POST.get('mode')
            trns.additional_charges = data.get("additionalCharges", 0)
            trns.field9 = request.POST.get('field9')
            trns.save()
            return redirect('payfailure')
        else:
            pass
    else:
        raise SuspiciousOperation("Invalid access")

    return redirect('payfailure')


@csrf_exempt
def cancel_payubiz(request):
    if request.method == "POST" or "GET":
        data = key_collect_payubiz(request)
        if verify_hash(data):
            trns = Transaction.objects.get(txnid=data['txnid'])
            trns.payment_id = request.POST.get('payuMoneyId')
            trns.payu_status = (request.POST.get('status') == 'success')  # Boolean
            trns.status = Transaction.CANCELLED
            trns.error_code = request.POST.get('error')  # should return no_error e000
            trns.error_message = request.POST.get('error_Message')
            trns.bank_refnum = request.POST.get('bank_ref_num')
            trns.mihpay_id = request.POST.get('mihpayid')
            trns.payment_added_on = request.POST.get('addedon')
            trns.pg_type = request.POST.get('PG_TYPE')
            trns.payment_mode = request.POST.get('mode')
            trns.additional_charges = data.get("additionalCharges", 0)
            trns.field9 = request.POST.get('field9')
            trns.save()
            reurl = reverse('index', args=(), kwargs={})
            return HttpResponseRedirect(reurl)
        else:
            pass
    else:
        raise SuspiciousOperation("Invalid access")
    return redirect('payfailure')


def payment_paypal(request, txnid):
    pass
