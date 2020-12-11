from people.models import ProfessionalServices
from rest_framework import serializers


class ProfessionalServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalServices
        fields = "__all__"