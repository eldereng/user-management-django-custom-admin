from people.models import ProfessionalServices
from rest_framework import serializers


class ProfessionalServicesSerializer(serializers.ModelSerializer):
    professional_name = serializers.CharField(required=False)

    class Meta:
        model = ProfessionalServices
        fields = "__all__"