from rest_framework import viewsets
from rest_framework.response import Response
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

    def retrieve(self, request, version, pk=None):
        queryset = SAQAQualification.objects.get(saqa_id=pk)
        serializer = SAQAQualificationSerializer(queryset)
        return Response(serializer.data)
