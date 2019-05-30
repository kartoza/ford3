from rest_framework import serializers
from ford3.models.qualification import Qualification
from api.serializers.qualification_event import QualificationEventSerializer
from api.serializers.subject import SubjectSerializer
from api.serializers.saqa_qualification import SAQAQualificationSerializer
from api.serializers.occupation import OccupationSerializer
from api.serializers.interest import InterestSerializer


class QualificationSerializer(serializers.ModelSerializer):
    qualification_events = QualificationEventSerializer(many=True)
    subjects = SubjectSerializer(many=True)
    saqa_qualification = SAQAQualificationSerializer()
    occupations = OccupationSerializer(many=True)
    interests = InterestSerializer(many=True)

    class Meta:
        model = Qualification
        fields = '__all__'
