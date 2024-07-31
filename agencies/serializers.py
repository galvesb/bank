from rest_framework import serializers
from agencies.models import Agency

class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = ['id', 'name', 'address', 'phone_number']
