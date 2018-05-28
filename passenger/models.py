from django.db import models
from driver.models import Destination, Pickup_Location
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Passenger(models.Model):
    rider_image = models.ImageField(upload_to = 'rider/',blank=True)
    rider_user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    email_confirmed = models.BooleanField(default=False)
    name= models.CharField(max_length=60)
    phone = models.CharField(max_length=100)
    final_destination = models.ForeignKey(Destination,null=True)
    pickup_point = models.ForeignKey(Pickup_Location,null=True)


    def __str__(self):
        return str(self.rider_user.username)

    def save_passenger(self):
        self.save()

    def delete_passenger(self):
        self.delete()

    def delete(self):
        self.email_confirmed = False
        self.save()

    @staticmethod
    def update_passenger(id,driver_image,name,phone):

        Passenger.objects.filter(pk=id).update(rider_image=rider_image,rider_user=rider_user,name=name,phone=phone)

# @receiver(post_save, sender=User)
# def update_user_passenger(sender, instance, created, **kwargs):
#     if created:
#         Passenger.objects.create(rider_user=instance)
#     instance.passenger.save()
