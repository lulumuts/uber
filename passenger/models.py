from django.db import models
from driver import Destination, Pickup_Location
# Create your models here.
class Passenger(models.Model):
    name= models.CharField(max_length=60)
    phone = models.CharField(max_digits=10)
    final_destination = models.Foreignkey(Destination)
    pickup_point = models.Foreignkey(Pickup_Location)
