from django.urls import path
from django.views.generic import TemplateView

from .views import succ_payubiz, failure_payubiz, cancel_payubiz, payment_payubiz

urlpatterns = [
    path('payubiz_success/', succ_payubiz, name="succ_paybiz"),
    path('failure_payubiz/', failure_payubiz, name="failure_payubiz"),
    path('cancel_payubiz/', cancel_payubiz, name="cancel_payubiz"),
    path('payubiz_entrance/', payment_payubiz, name="payubiz_entrance"),
    path('paymentsuccess/', TemplateView.as_view(template_name="payment/success.html"), name='paysuccess'),
    path('paymentfailure/', TemplateView.as_view(template_name="payment/failure.html"), name='payfailure'),
]
