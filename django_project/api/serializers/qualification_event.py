from rest_framework import serializers
from ford3.models.qualification_event import QualificationEvent


class QualificationEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationEvent
        fields = '__all__'
