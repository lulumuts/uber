from django.contrib import admin
from .models import Passenger
from django.contrib.gis import admin
from django.forms import ModelForm
from django import forms
from leaflet.admin import LeafletGeoAdmin


admin.site.register(Passenger)
