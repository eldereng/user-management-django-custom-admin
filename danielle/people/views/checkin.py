from people.models import Checkin
from people.serializers import CheckinSerializer, CheckinSerializerWhithoutReasonField
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class CheckinViewSet(viewsets.ModelViewSet):
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
    filter_backends = [
        filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter
    ]
    search_fields = ['person__name']
    filterset_fields = ['active']
    ordering_fields = ['created_at']
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'PATCH':
            serializer_class = CheckinSerializerWhithoutReasonField
        return serializer_class


"""
    # check if there's an active checkin
    peopleWithCheckinActive = Checkin.objects.filter(
        person_id=data['person'].id, active=True)
    if peopleWithCheckinActive:
        raise serializers.ValidationError(
            {'person': 'Essa pessoa tem um checkin ativo.'})
    return data
"""
