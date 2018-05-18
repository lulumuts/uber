from django.conf.urls import url
from . import views
from django.conf import settings

app_name = "driver"

urlpatterns=[

    url('^$',views.driver_home,name='driver_home')
]
