from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^annotated/static/(?P<path>.*)$', 'django.views.static.serve', 
           {'document_root': settings.STATIC_URL2}),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
    url(r'^annotated/(.*)$', 'cms_templates.views.withTemplates'),
    url(r'^(.*)$', 'cms_templates.views.processCmsRequest'),
)
