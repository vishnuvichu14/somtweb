# Generated by Django 3.0.6 on 2020-05-22 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=12, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Milking'), (1, 'Packed'), (2, 'Out for delivery'), (3, 'Delivered'), (4, 'Cancelled'), (5, 'SKIPPED')], default=0)),
                ('message', models.CharField(max_length=1024)),
                ('delivered_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=128)),
                ('quantity', models.FloatField()),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('is_paid', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('payment_mode', models.IntegerField(choices=[(0, 'Cash'), (1, 'Card'), (2, 'Payubiz')])),
                ('status', models.IntegerField(choices=[(0, 'Initiated'), (1, 'Paid'), (2, 'Cancelled'), (3, 'Failed'), (4, 'Refund_initiated'), (5, 'Refund_finished')])),
                ('txnid', models.CharField(max_length=30, null=True)),
                ('error_code', models.CharField(max_length=255, null=True)),
                ('error_message', models.CharField(max_length=255, null=True)),
                ('bank_refnum', models.CharField(max_length=255, null=True)),
                ('refund_amount', models.IntegerField(default=0, null=True)),
                ('additional_charges', models.FloatField(default=0, null=True)),
                ('field9', models.TextField(max_length=512, null=True)),
                ('payment_added_on', models.DateTimeField(null=True)),
                ('pg_type', models.CharField(max_length=255, null=True)),
                ('payment_id', models.CharField(max_length=10, null=True)),
                ('payu_status', models.BooleanField(default=0)),
                ('mihpay_id', models.CharField(max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paid_by', to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_order', to='payment.Order')),
            ],
        ),
    ]