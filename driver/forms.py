from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from leaflet.forms.fields import PointField
from .models import Driver,Pickup_Location
from leaflet.forms.widgets import LeafletWidget


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class MapsForm(forms.ModelForm):

    class Meta:
        model = Pickup_Location
        fields = ('name', 'location')
