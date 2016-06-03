from django.conf.urls import patterns, include, url
from blog.models import *
from blog.views import *

urlpatterns = patterns('',
   url(r'^post/(?P<id_post>\d+)/$', 
       'blog.views.post', 
       name='post'),
   url(r"", "blog.views.main"),
)