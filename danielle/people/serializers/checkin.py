from people.models import Checkin
from rest_framework import serializers


class CheckinSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['reason'] == 'patient':
            if 'companion' not in data.keys():
                raise serializers.ValidationError(
                    {'companion': 'Todo paciente deve ter acompanhante.'})
        return data

    class Meta:
        model = Checkin
        fields = '__all__'
