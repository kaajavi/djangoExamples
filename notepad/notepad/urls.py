from django.conf.urls import patterns, include, url
from django.views.generic.edit import UpdateView

urlpatterns = patterns('',
                       url(r'^$', 
                           'notepad.views.home', 
                           name='home'),
                       url(r'^notas/(?P<id_nota>\d+)/$', 
                           'notepad.views.nota', 
                           name='nota'),
                      )