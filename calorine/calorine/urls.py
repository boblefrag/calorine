from django.conf.urls import patterns, include, url
from django.shortcuts import redirect

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
                       url(r'^accounts/', include('registration.urls')),
                       url(r'^accounts/profile/$', 'calorine.caro.views.profile'),
                       url(r'^songs/$', 'calorine.caro.views.songs'),
                       url(r'^logs$', 'calorine.caro.views.logs'),
                       url(r'^playlist/add/(?P<song_id>\d+)$', 'calorine.caro.views.pladd'),
                       url(r'^$', 'calorine.caro.views.playlist')
                       )
# Examples:
# url(r'^$', 'calorine.views.home', name='home'),
# url(r'^calorine/', include('calorine.foo.urls')),
# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
# Uncomment the next line to enable the admin:
# url(r'^admin/', include(admin.site.urls)),
