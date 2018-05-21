from django.conf.urls import url
from . import views as core_views
from django.conf import settings


app_name = "driver"

urlpatterns=[

    url('^$',core_views.driver_home,name='driver_home'),
    url(r'^signup/$', core_views.signup, name='signup'),
    
]
