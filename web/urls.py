from django.contrib import admin
from django.urls import path

from .views import landing_page,order_payment_page

urlpatterns = [
    path('', landing_page, name="landing_page"),
    path('order_pay/', order_payment_page, name="order_payment_page"),
]