from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from application.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', pdf_converter),
    #url(r'^$', generate_pdf_view),
    # url(r'^blog/', include('blog.urls')),
    url(r'^/upload_file/$', pdf_converter),
    url(r'^admin/', include(admin.site.urls)),
)
