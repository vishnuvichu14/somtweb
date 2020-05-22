from datetime import timedelta

from django.contrib.auth.models import User, Group
from web.models import Farm, Breed, Worker, Cow, Milk, Profile
from payment.models import Order
from django.utils import timezone

breed_1 = Breed.objects.create(name="Breed 1")
breed_1.description = "No Description"
breed_1.save()

breed_2 = Breed.objects.create(name="Breed 2")
breed_2.description = "No Description"
breed_2.save()

group1 = Group.objects.get(name="Customer")
group2 = Group.objects.get(name="Admin")
group3 = Group.objects.get(name="Worker")

customer_user_1 = Profile.objects.create(username="Customer1", email="customer1@gmail.com", phone="123456789")
customer_user_1.set_password("helloworld@123")
customer_user_1.save()

worker_user_1 = Profile.objects.create(username="Worker1", email="worker1@gmail.com", phone="123456789")
worker_user_1.set_password("helloworld@123")
worker_user_1.save()

group1.user_set.add(customer_user_1.user)
group3.user_set.add(worker_user_1.user)

farm_1 = Farm.objects.create(name="Farm 1", address="Farm Address 1", latitude=1, longitude=1, pin_code="123")

cow_1 = Cow.objects.create(farm=farm_1, name="Cow 1", tag="123", date_of_birth=timezone.now(), breed=breed_1,
                           default_quantity="25")
cow_2 = Cow.objects.create(farm=farm_1, name="Cow 2", tag="456", date_of_birth=timezone.now(), breed=breed_2,
                           default_quantity="30")

Worker.objects.create(user=worker_user_1, farm=farm_1)

Milk.objects.create(cow=cow_1, quantity="25", date=timezone.now())

order_1 = Order.objects.create(farm=farm_1, cow=cow_1, customer=customer_user_1, order_number="1", quantity=40,
                               amount=58,
                               start_date=timezone.now(), end_date=(timezone.now() + timedelta(1)))
