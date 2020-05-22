from django.db import models
from datetime import date

from django.db.models import Sum, Count


class Farm(models.Model):
    name = models.CharField(max_length=1024, null=True, blank=True)
    address = models.CharField(max_length=2048, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    pin_code = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        string = ""
        if self.name:
            string += self.name
        string += " "
        return string + str(self.pin_code)

    def get_total_number_of_cows(self):
        return Count(Cow.objects.filter(farm_id=self.id))

    def get_total_number_of_worker(self):
        pass


class Cow(models.Model):
    name = models.CharField(max_length=1024)
    tag = models.CharField(max_length=1024)
    date_of_birth = models.DateTimeField(null=False)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, related_name="breed")
    create_at = models.DateTimeField(auto_now=True)
    farm = models.ForeignKey('Farm', on_delete=models.CASCADE, related_name="farm")
    default_quantity = models.CharField(max_length=1024, null=True)
    photo = models.ImageField(upload_to='cow_photo/', null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_code/', null=True, blank=True)

    def __str__(self):
        string = ""
        if self.name:
            string += " " + self.name
            string += " "
        if self.farm:
            string += self.farm.pin_code
        string += " " + self.breed.name
        return string

    def get_age(self):
        date_of_birth = self.date_of_birth
        today = date.today()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        return age

    def get_average_milk_quantity(self):
        milk_objs = Milk.objects.filter(cow_id=self.id)
        milk_objs_sum = milk_objs.aggregate(Sum('quantity'))['quantity__sum']
        return str(float(milk_objs_sum) / float(len(milk_objs)))


class Breed(models.Model):
    name = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=2048, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Milk(models.Model):
    cow = models.ForeignKey('Cow', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=256, null=False)
    date = models.DateTimeField(null=False)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.cow.tag) + " " + str(self.quantity) + " " + str(self.date)


class Worker(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user")  # which user is worker
    farm = models.ForeignKey('Farm', on_delete=models.CASCADE, related_name="farm")  # belong to which farm

    def __str__(self):
        return self.user.username + " " + self.farm.pin_code
