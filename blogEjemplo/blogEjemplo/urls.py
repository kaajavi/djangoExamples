from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.main', name='home'),    
    url(r'^admin/', include(admin.site.urls)), 
)