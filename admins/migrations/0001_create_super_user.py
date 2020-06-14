from __future__ import unicode_literals
from django.db import migrations, models
from django.contrib.auth.models import User, Group
from django.utils import timezone
import pytz


def forwards_func(apps, schema_editor):
    super_user = User.objects.create(username='somtadmin', email='somtadmin@gmail.com', last_login=timezone.now(),
                                     is_superuser=True, is_staff=True)
    super_user.set_password('milkandtrack')
    super_user.save()
    group1 = Group.objects.create(name="Customer")
    group2 = Group.objects.create(name="Admin")
    group3 = Group.objects.create(name="Worker")
    group1.user_set.add(super_user)
    group2.user_set.add(super_user)
    group3.user_set.add(super_user)


def reverse_func(apps, schema_editor):
    super_user = User.objects.get(username='smotadmin')
    super_user.delete()
    group1 = Group.objects.get(name="Customer")
    group2 = Group.objects.get(name="Admin")
    group3 = Group.objects.get(name="Worker")
    group1.delete()
    group2.delete()
    group3.delete()


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
