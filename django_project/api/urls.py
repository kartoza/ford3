from django.conf.urls import url
from rest_framework import routers
from api.viewsets.provider import ProviderViewSet
#
# router = routers.SimpleRouter()
# router.register(
#     r'^(?P<version>(v1))/providers',
#     ProviderViewSet,
#     'show-providers-api')
urlpatterns = [
    url(r'^(?P<version>(v1))/providers',
        ProviderViewSet.as_view({'get': 'list'}),
        name='show-providers-api')
]
