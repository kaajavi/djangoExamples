from django.conf.urls import patterns, include, url
from blog.models import *
from blog.views import *

urlpatterns = patterns('',
   (r"^(\d+)/$", "post"),
   (r"^add_comment/(\d+)/$", "add_comment"),
   (r"^delete_comment/(\d+)/$", "delete_comment"),
   (r"^delete_comment/(\d+)/(\d+)/$", "delete_comment"),
   (r"^month/(\d+)/(\d+)/$", "month"),
   (r"", "blog.main"),
)