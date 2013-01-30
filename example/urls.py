from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fussverkehr.views.home', name='home'),
    # url(r'^fussverkehr/', include('fussverkehr.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^test/', 'quiz.views.get_json'),
	url(r'^timestamp/', 'quiz.views.get_timestamp'),
	url(r'^admin/', include(admin.site.urls)),
)