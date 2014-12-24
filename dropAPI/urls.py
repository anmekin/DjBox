__author__ = 'andrey'
from django.conf.urls import patterns, url
from views import *
from ajax import *

urlpatterns = patterns('',

    url(r'^$', home, name='home'),
    url(r'^upload/$', upload, name="upload"),
    url(r'^userfiles/$', userfiles, name='userfiles'),
    url(r'^userfiles_ajax/$', userfiles_ajax, name='userfiles_ajax'),
    url(r'^show_file/$', show_file, name='show_file'),

)

