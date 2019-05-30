from rest_framework import serializers
from ford3.models.campus_event import CampusEvent


class CampusEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = CampusEvent
        fields = '__all__'
