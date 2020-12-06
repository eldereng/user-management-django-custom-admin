from people.models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    formatted_born_date = serializers.CharField()

    class Meta:
        model = Person
        fields = "__all__"
        extra_kwargs = {'formatted_born_date': {'read_only': True}}
