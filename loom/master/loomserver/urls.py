from django.conf import settings
from django.conf.urls import patterns, include, url
import django.views.static

urlpatterns = [
    url(r'^api/', include('analysis.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
"""
if settings.DEBUG == True:
    # Static files should not be served like this in production
    urlpatterns += patterns(
        '',
        url(
            r'^$',
            django.views.static.serve,
            {
                'path':'index.html',
                'document_root': settings.DOC_ROOT
            }
        ),
        url(r'^favicon\.ico$',
            django.views.static.serve,
            {
                'path':'favicon.ico',
                'document_root': settings.DOC_ROOT
            }
        ),
        url(
            r'^(?P<path>.*)$',
            django.views.static.serve,
            {
                'document_root': settings.DOC_ROOT
            }
        ),
    )
"""
