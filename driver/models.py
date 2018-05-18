from django.db import models

class Destination(models.Model):
    name= models.CharField(max_length=100)

class Car(models.Model):
    brand = models.CharField(max_length=100)
    num_plate = models.CharField(max_length=60)
    num_of_seats= models.IntegerField(max_digits=8)

class Pickup_Location(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=100)
    car = models.Foreignkey
    passenger_pickup = models.Foreignkey(Pickup_Location)
    phone = models.IntegerField(max_digits=10)
    destination = models.Foreignkey(Destination)
