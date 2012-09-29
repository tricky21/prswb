# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uxperiment.views.home', name='home'),
    # url(r'^uxperiment/', include('uxperiment.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pages.views.dashboard', name='dashboard'),
    url(r'^contact', 'pages.views.contact', name='contact'),
    url(r'^contact/merci', 'pages.views.confirm_contact',
        name='confirm_contact'),

    #url(r'^proposer-un-site', 'websites.views.propose',
    #    name='propose_website'),

    url(r'^pages/(?P<slug>[-\w\d]+)/$', 'pages.views.markdown_page',
        name='markdown_page'),
)

urlpatterns += staticfiles_urlpatterns()
