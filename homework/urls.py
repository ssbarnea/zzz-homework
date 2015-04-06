from django.conf.urls import include, url
from django.contrib import admin


from views import main

urlpatterns = [
    # Examples:
    url(r'^(?P<topic>[^\/]+)/(?P<user>[^\/]+)/?$', main.page),
    url(r'^(?P<topic>[^\/]+)/?$', main.post_message),
    url(r'^$', main.fallback, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
