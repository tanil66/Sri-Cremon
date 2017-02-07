__author__ = 'rt'

from django.conf.urls import patterns, url, include
from myproject import views
from django.conf import settings
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                url(r'^about$', views.about, name='about'),
                url(r'^admission$', views.admission, name='admission'),
                url(r'^events$', views.events, name='events'),       
                url(r'^contact$', views.contact, name='contact'),
                url(r'^holiday$', views.holiday, name='holiday'),
                url(r'^management$', views.management, name='management'),
                url(r'^testmonials$', views.testmonials, name='testmonials'),       
                url(r'^resource$', views.resource, name='resource'),
                url(r'^images$', views.images, name='images'),
		url(r'^highlights$', views.highlights, name='highlights'),       
                url(r'^program$', views.program, name='program'),
		url(r'^branches$', views.branches, name='branches'),
		url(r'^calendar$', views.calendar, name='calendar'),
		url(r'^gallery$', views.gallery, name='gallery'),
                url(r'^videos$', views.videos, name='videos'),
                url(r'^photos$', views.photos, name='photos'),       
		url(r'^holiday$', views.holiday, name='holiday'),
		url(r'^newdesign$', views.newdesign, name='newdesign'),
		url(r'^information$', views.information, name='information'),
                #url(r'^login', views.login, name='login'),
                #url(r'^registration_form', views.registration_form, name='registration_form'),       
                       
		      
)
