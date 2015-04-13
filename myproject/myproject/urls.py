from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
    url(r'^annotated/(.*)$', 'cms_templates.views.withTemplates'),
    url(r'^(.*)$', 'cms_templates.views.processCmsRequest'),
)
