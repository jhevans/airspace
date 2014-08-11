from radar import views

__author__ = 'johnh.evans'
from django.conf.urls import patterns, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^radar/$', views.radar, name='radar'),
)

