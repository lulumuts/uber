from django.conf.urls import url
from . import views
from django.conf import settings
app_name = "passenger"

urlpatterns=[

    url('^$',views.passenger_home,name='passenger_home'),
]
