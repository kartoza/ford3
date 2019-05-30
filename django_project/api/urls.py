from django.urls import path
from api.viewsets.provider import ProviderViewSet


urlpatterns = [
    path(r'^(?P<version>(v1))/providers',
         ProviderViewSet.as_view({'get': 'list'}),
         name='show-providers-api')
]
