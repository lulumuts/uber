from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.gis.db.models.proxy import SpatialProxy
from django.dispatch import receiver
from django.contrib.gis.geos import (
    GeometryCollection, GEOSException, GEOSGeometry, LineString,
    MultiLineString, MultiPoint, MultiPolygon, Point, Polygon
)




class Destination(models.Model):
    name= models.CharField(max_length=100)


    def __str__(self):
        return str(self.name)

    def save_destination(self):
        self.save()

    def delete_destination(self):
        self.delete()


class Car(models.Model):
    brand = models.CharField(max_length=100)
    num_plate = models.CharField(max_length=60)
    num_of_seats= models.IntegerField()


    def __str__(self):
        return str(self.brand)

    def save_car(self):
        self.save()

    def delete_car(self):
        self.delete()


class Pickup_Location(models.Model):
    name=models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    geom=models.PointField(srid=4326)
    objects=models.GeoManager()


    def __str__(self):
        return str(self.name)

    def save_pickup(self):
        self.save()

    def delete_pickup(self):
        self.delete()

# Create your models here.
class Driver(models.Model):
    driver_user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    car = models.ForeignKey(Car,null=True)
    passenger_pickup = models.ManyToManyField(Pickup_Location)
    phone = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination,null=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def save_driver(self):
        self.save()

    def delete_driver(self):
        self.delete()

    def delete(self):
        self.email_confirmed = False
        self.save()

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Driver.objects.create(driver_user=instance)
    instance.driver.save()
