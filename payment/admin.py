from django.contrib import admin
from payment.models import Transaction,Order,Delivery

admin.site.register(Transaction)
admin.site.register(Order)
admin.site.register(Delivery)
