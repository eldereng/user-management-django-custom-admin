from people.models import HomeServices
from rest_framework import serializers


class HomeServicesSerializer(serializers.ModelSerializer):
    person_name = serializers.CharField(required=False)

    class Meta:
        model = HomeServices
        fields = "__all__"