from people.models import Checkin
from people.serializers import CheckinSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class CheckinViewSet(viewsets.ModelViewSet):
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # search_fields = ['name']
    # ordering_fields = ['name']
    permission_classes = [IsAuthenticated]


"""
    # check if there's an active checkin
    peopleWithCheckinActive = Checkin.objects.filter(
        person_id=data['person'].id, active=True)
    if peopleWithCheckinActive:
        raise serializers.ValidationError(
            {'person': 'Essa pessoa tem um checkin ativo.'})
    return data
"""
