from rest_framework import viewsets
from ford3.models.provider import Provider
from api.serializers.provider import ProviderSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
