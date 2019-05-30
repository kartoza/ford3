from rest_framework import serializers
from ford3.models.provider import Provider


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ('name', 'email')
