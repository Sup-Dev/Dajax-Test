from django.conf.urls import patterns, include, url

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'examples.views.index', name='index'),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
