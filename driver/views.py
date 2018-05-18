from django.shortcuts import render

# Create your views here.
def driver_home(request):
    return render(request, 'home.html')
