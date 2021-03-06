from django.shortcuts import render,redirect
from .forms import SignUpForm
from .models import Passenger
from .tokens import account_activation_token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from driver.models import Destination,Driver,Car
from django.http import Http404
from .forms import DestinationForm


# Create your views here.
def passenger_home(request):
    return render(request, 'passenger/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            profile= Passenger.objects.create(rider_user=user)
            profile.save()

            current_site = get_current_site(request)
            subject = 'Activate your Uber Account'
            message = render_to_string('passenger/account_activation_email.html',{
                'user' : user,
                'domain' : current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.passenger.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'passenger/account_activation_invalid.html')

def account_activation_sent(request):
    current_user = request.user
    if current_user.is_authenticated():
        return redirect('account_activation_sent')
    return render(request, 'passenger/account_activation_sent.html')

def search_destination(request):
    all_places=Destination.objects.all()
    all_drivers=Car.objects.all()
    print(all_places)
    return render(request, 'passenger/going.html',{'all_places':all_places,"all_drivers":all_drivers})

def single_driver(request,car_user):
    current_user = request.user
    # userProfile = Driver.objects.filter(driver_user=current_user).first()
    car = Car.objects.filter(car_user=current_user).first()
    print(car)

    current_user = request.user
    if request.method == 'POST':
        form= DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            destination = form.save(commit = False)

            UserProfile= User.objects.filter(username=current_user).first()
            destination.driver_place=UserProfile
            destination.save()

    else:
        form = DestinationForm()

    return render(request, 'passenger/details.html', {"car":car,"form":form})

def destination(request):
    current_user = request.user
    if request.method == 'POST':
        form= DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            destination = form.save(commit = False)

            UserProfile= User.objects.filter(username=current_user).first()
            destination.driver_place=UserProfile
            destination.save()

    else:
        form = DestinationForm()
    return render(request, 'passenger/details.html',{"form":form})
