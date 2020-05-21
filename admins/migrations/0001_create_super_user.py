from __future__ import unicode_literals
from django.db import migrations, models
from django.contrib.auth.models import User
from django.utils import timezone
import pytz


def forwards_func(apps, schema_editor):
    super_user = User.objects.create(username='somtadmin', email='somtadmin@gmail.com', last_login=timezone.now(),
                                     is_superuser=True, is_staff=True)
    super_user.set_password('milkandtrack')
    super_user.save()


def reverse_func(apps, schema_editor):
    super_user = User.objects.get(username='smotadmin')
    super_user.delete()


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
