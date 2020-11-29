from people.models import Person
from rest_framework import serializers

from utils.cpf.check_cpf import check_cpf
from utils.format_numerical_text import format_numerical_text


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate_cpf(self, value):
        if not check_cpf(value):
            raise serializers.ValidationError("CPF inválido.")
        return format_numerical_text(value)
