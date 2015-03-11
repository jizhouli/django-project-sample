from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# import self-defined module
from mysite.views import hello, current_datetime, hours_ahead
from books import views
from contact.views import contact, contact_thanks

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', contact),
    url(r'^contact/thanks/$', contact_thanks),
)
