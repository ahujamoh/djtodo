from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$', 'todoapp.views.home', name='home'),
    url(r'^stats', 'todoapp.views.stats', name='stats'),
    url(r'^search', 'todoapp.views.search', name='search results'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
