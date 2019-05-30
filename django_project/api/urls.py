from django.conf.urls import url
from rest_framework import routers
from api.viewsets.provider import ProviderViewSet

router = routers.SimpleRouter()
router.register(r'^(?P<version>(v1))/providers', ProviderViewSet)
urlpatterns = router.urls
