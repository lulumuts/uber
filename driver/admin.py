from django.contrib import admin
from .models import Destination,Car,Pickup_Location,Driver
from django.contrib.gis import admin
from django.forms import ModelForm
from django import forms
from leaflet.admin import LeafletGeoAdmin


admin.site.register(Destination)
admin.site.register(Car)
admin.site.register(Pickup_Location,LeafletGeoAdmin)
admin.site.register(Driver)
