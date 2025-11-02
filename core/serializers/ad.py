from rest_framework import serializers
from core.models import Ad

class AdSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    active = serializers.BooleanField(default=True)

    class Meta:
        model = Ad
        fields = ['id', 'user', 'category', 'city', 'title', 'description', 'price', 'image', 'slug', 'active', 'created_at', 'updated_at']

    def validate_title(self, data: str):
        if data.isnumeric():
            raise serializers.ValidationError('Title must contain alphabet')
        elif len(data) < 2:
            raise serializers.ValidationError('Title must contain at least two letters')
        return data

    def validate_description(self, data: str):
        if data.isnumeric():
            raise serializers.ValidationError('Description must contain alphabet')
        elif len(data) < 10:
            raise serializers.ValidationError('Description must contain at least ten character')