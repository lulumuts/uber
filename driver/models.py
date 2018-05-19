from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Destination(models.Model):
    name= models.CharField(max_length=100)

class Car(models.Model):
    brand = models.CharField(max_length=100)
    num_plate = models.CharField(max_length=60)
    num_of_seats= models.IntegerField()

class Pickup_Location(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

# Create your models here.
class Driver(models.Model):
    driver_user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    car = models.ForeignKey(Car,null=True)
    passenger_pickup = models.ForeignKey(Pickup_Location)
    phone = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination)

    def __str__(self):
        return str(self.user)

    def save_driver(self):
        self.save()

    def delete_driver(self):
        self.delete()

    def delete(self):
        self.email_confirmed = False
        self.save()

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Driver.objects.create(driver_user=instance)
#     instance.profile.save()
