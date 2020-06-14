from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from web.models import Cow, Farm, Worker


class Transaction(models.Model):
    INITIATED = 0
    PAID = 1
    CANCELLED = 2
    FAILED = 3
    REFUND_INITIATED = 4
    REFUND_FINISHED = 5

    CASH = 0
    CARD = 1
    PAYUBIZ = 2

    STATUS_CHOICES = ((INITIATED, "Initiated"), (PAID, "Paid"), (CANCELLED, "Cancelled"), (FAILED, "Failed"),
                      (REFUND_INITIATED, "Refund_initiated"), (REFUND_FINISHED, "Refund_finished"))
    PAYMENT_METHOD = ((CASH, "Cash"), (CARD, "Card"), (PAYUBIZ, 'Payubiz'))

    amount = models.DecimalField(max_digits=10, decimal_places=3)
    payment_mode = models.IntegerField(choices=PAYMENT_METHOD)
    status = models.IntegerField(choices=STATUS_CHOICES)
    txnid = models.CharField(max_length=30, null=True)

    error_code = models.CharField(max_length=255, null=True)
    error_message = models.CharField(max_length=255, null=True)
    bank_refnum = models.CharField(max_length=255, null=True)
    refund_amount = models.IntegerField(default=0, null=True)
    additional_charges = models.FloatField(default=0, null=True)
    field9 = models.TextField(max_length=512, null=True)
    payment_added_on = models.DateTimeField(null=True)
    pg_type = models.CharField(max_length=255, null=True)
    payment_id = models.CharField(max_length=10, null=True)
    payu_status = models.BooleanField(default=0)
    mihpay_id = models.CharField(max_length=30, null=True)

    customer = models.ForeignKey(User, related_name='paid_by', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='transaction_order')

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True)

    def update(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer.username)


class Order(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="order_farm")
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE, related_name="order_cow")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_customer")

    order_number = models.CharField(max_length=128)
    quantity = models.FloatField()
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    is_paid = models.BooleanField(default=False)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.customer.username) + " " + str(self.cow.tag) + " " + str(self.is_paid)


class Delivery(models.Model):
    MILKING = 0
    PACKED = 1
    OUT_FOR_DELIVERY = 2
    DELIVERED = 3
    CANCELLED = 4
    SKIPPED = 5
    STATUS_CHOICE = (
        (MILKING, 'Milking'), (PACKED, 'Packed'), (OUT_FOR_DELIVERY, 'Out for delivery'), (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'), (SKIPPED, 'SKIPPED'))

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="delivery_order")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_query_name='worker')

    quantity = models.CharField(max_length=12, null=True)
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)
    message = models.CharField(max_length=1024)
    delivered_time = models.DateTimeField()
