__author__ = 'andrey'
#coding: utf-8
from django.conf.urls import patterns, url
from loginsys.views import login, logout, signup

urlpatterns = patterns('',
    url(r'login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),
)
