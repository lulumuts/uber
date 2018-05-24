from django.conf.urls import url,include
from . import views as core_views
from django.conf import settings
from django.contrib.auth import views
from django.contrib.auth.views import logout



app_name = "driver"

urlpatterns=[

    url('^$',core_views.driver_home,name='driver_home'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^maps/$',core_views.map_view, name='map_view'),
    url(r'^pickup/$',core_views.pickup, name='pickup')

]
