# coding=utf-8
"""Project level url handler."""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.shortcuts import render
from sentry_sdk import capture_message
# from django.conf.urls.static import static

admin.autodiscover()
handler404 = 'base.views.error_views.custom_404'


def handler500(request, template_name='500.html', *args, **kwargs):
    """500 error handler which includes ``request`` in the context.

    See http://raven.readthedocs.org/en/latest/integrations/
        django.html#message-references

    :param request: Django request object.

    Templates: `500.html`
    Context: None
    """
    capture_message("Page not found!", level="error")

    # You need to create a 500.html template.
    response = render(
        request,
        template_name,
        context={
            'request': request
        },
        status=500)
    return response


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^site-admin/', admin.site.urls),
    url(r'^ford3/', include('ford3.urls')),
    url(r'^', include('base.urls')),
    # url(r'^', include('ford3.urls')),
    # url(r'^accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
