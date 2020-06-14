from django.contrib.auth.models import User
from rest_framework import serializers

from web.models import Farm,Cow
from payment.models import Transaction,Order