from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
# from leaflet.forms.fields import PointField
from .models import Passenger
from driver.models import Destination

# from leaflet.forms.widgets import LeafletWidget


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=60)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','phone')

class DestinationForm(forms.ModelForm):

    class Meta:
        model= Destination
        exclude = ['driver_place','place']

        widgets = {
            'pickups' : forms.RadioSelect
        }
