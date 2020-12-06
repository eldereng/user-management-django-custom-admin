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
