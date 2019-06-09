from rest_framework import viewsets
from ford3.models.saqa_qualification import SAQAQualification
from api.serializers.saqa_qualification import SAQAQualificationSerializer


class SAQAQualificationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    Returns a SAQA qualification for a given ID.

    list:
    Returns a list of all SAQA qualifications registered with OpenEdu.
    """
    queryset = SAQAQualification.objects.all()
    serializer_class = SAQAQualificationSerializer
