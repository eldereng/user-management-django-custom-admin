from people.models import Checkin
from rest_framework import serializers


class CheckinSerializer(serializers.ModelSerializer):
    companion_name = serializers.CharField(required=False)
    person_name = serializers.CharField(required=False)
    formatted_created_at = serializers.CharField(required=False)

    def validate(self, data):
        # check if patient have a companion
        if data['reason'] == 'patient':
            if 'companion' not in data.keys():
                raise serializers.ValidationError(
                    {'companion': 'Todo paciente deve ter acompanhante.'})
            else:
                if not data['companion']:
                    raise serializers.ValidationError(
                        {'companion': 'Campo acompanhante não pode ser nulo.'})
        return data

    class Meta:
        model = Checkin
        exclude = ['updated_at', 'created_at']
        extra_kwargs = {
            'formatted_born_date': {
                'read_only': True
            },
            'companion_name': {
                'read_only': True
            },
            'patiente_name': {
                'read_only': True
            }
        }
