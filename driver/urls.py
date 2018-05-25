from django.conf.urls import url,include
from . import views as core_views
from django.conf import settings
from django.contrib.auth import views
from django.contrib.auth.views import logout
from django.conf.urls.static import static



app_name = "driver"

urlpatterns=[

    url('^$',core_views.driver_home,name='driver_home'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^maps/$',core_views.map_view, name='map_view'),
    url(r'^pickup/$',core_views.pickup, name='pickup'),
    url(r'^start/$',core_views.full_display, name='start'),
    url(r'^profile/$', core_views.new_car, name='profile'),
    url(r'^destination/$',core_views.destination,name='destination'),
    url(r'^start/$',core_views.to_display,name='start'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
