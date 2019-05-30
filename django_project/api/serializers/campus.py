from rest_framework import serializers
from ford3.models.campus import Campus
from api.serializers.campus_event import CampusEventSerializer
from api.serializers.qualification import QualificationSerializer


class CampusSerializer(serializers.ModelSerializer):
    campus_events = CampusEventSerializer(many=True)
    campus_qualifications = QualificationSerializer(many=True)

    class Meta:
        model = Campus
        fields = '__all__'
