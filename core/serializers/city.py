from rest_framework import serializers
from core.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'created_at', 'updated_at']

    def validate_name(self, data: str):
        if data.isnumeric():
            raise serializers.ValidationError('Name must contain alphabet')
        elif len(data) < 2:
            raise serializers.ValidationError('Name must contain at least two letters')
        return data