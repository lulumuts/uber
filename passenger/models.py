from django.db import models
from driver.models import Destination, Pickup_Location
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Passenger(models.Model):
    driver_image = models.ImageField(upload_to = 'rider/',blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    name= models.CharField(max_length=60)
    phone = models.IntegerField()
    final_destination = models.ForeignKey(Destination,null=True)
    pickup_point = models.ForeignKey(Pickup_Location,null=True)

# @receiver(post_save, sender=User)
# def update_user_passenger(sender, instance, created, **kwargs):
#     if created:
#         Passenger.objects.create(user=instance)
#     instance.passenger.save()
