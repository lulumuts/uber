from django.conf.urls import url
from . import views as core_views
from django.conf import settings


app_name = "driver"

urlpatterns=[

    url('^$',core_views.driver_home,name='driver_home'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),

]
