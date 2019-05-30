from rest_framework import serializers
from ford3.models.provider import Provider
from api.serializers.campus import CampusSerializer


class ProviderSerializer(serializers.ModelSerializer):

    campus = CampusSerializer(many=True)

    class Meta:
        model = Provider

        fields = '__all__'
