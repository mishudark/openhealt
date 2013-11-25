from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'framework.views.home', name='home'),
    # url(r'^framework/', include('framework.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'dashboard.views.index'),
    url(r'^pacient/update/$', 'pacients.views.update'),
    url(r'^pacient/list/$', 'pacients.views.list'),
    url(r'^question/update/$', 'questions.views.update'),
    url(r'^question/list/$', 'questions.views.list'),
    url('^accounts/login/$', login, {'template_name': 'login.html'}, name='log-in'),
    #url('^accounts/reset/$', password_reset, {'template_name': 'login.html'}, name='log-in'),
)
