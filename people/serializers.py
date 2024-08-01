from rest_framework import serializers
from .models import Person
from agencies.serializers import AgencySerializer

class PersonSerializer(serializers.ModelSerializer):
    agency = AgencySerializer()

    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'balance', 'agency']

class PersonCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'agency']
