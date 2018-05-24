from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes,force_text
from .models import Driver,Pickup_Location
from django.core.serializers import serialize
from django.http import HttpResponse




def driver_home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            print(user)
            current_site = get_current_site(request)
            subject = 'Activate your Uber Account'
            message = render_to_string('driver/account_activation_email.html',{
                'user' : user,
                'domain' : current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.driver.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'driver/account_activation_invalid.html')

def account_activation_sent(request):
    current_user = request.user
    if current_user.is_authenticated():
        return redirect('account_activation_sent')
    return render(request, 'driver/account_activation_sent.html')

'''
A function that processes the car registration information

def car_registry(request):

def destination(request):

'''

def map_view(request):
    pickups=serialize('geojson',Pickup_Location.objects.all())
    print(pickups)
    return HttpResponse(pickups, content_type="json")

def pickup(request):
    pickups=Pickup_Location.objects.all()
    print(pickups)
    return render(request, 'driver/pickup.html',{'pickups':pickups})

@login_required(login_url='/accounts/login/')
def new_driver(request):
    current_user = request.user
    if request.method == 'POST':
        form= DriverForm(request.POST, request.FILES)
        if form.is_valid():
            driver = form.save(commit = False)
            driver.driver_user = current_user
            driver.save()
    else:
        form = DriverForm()
    return render(request, 'driver/profile.html',{"form":form})
