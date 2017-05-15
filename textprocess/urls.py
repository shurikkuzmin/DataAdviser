from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

import views

urlpatterns = patterns('',
     url(r'^$', views.main_page, name='main'),
     url(r'^process/$',views.process_text, name='text-process'),
     url(r'^contact/$',views.contact, name='contact'),
     url(r'^submittoemail/$',views.submit_to_email, name='submit_to_email'),
     url(r'^replay/(?P<pkid>\d+)/$', views.replay_search, name='replay_view'),
)

