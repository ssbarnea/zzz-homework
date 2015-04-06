from django.conf.urls import include, url
from django.contrib import admin

import views

urlpatterns = [
    # Examples:
    url(r'^(?P<topic>[^\/]+)/(?P<user>[^\/]+)/?$', views.page),
    url(r'^(?P<topic>[^\/]+)/?$', views.post_message),
    url(r'^$', views.fallback, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
