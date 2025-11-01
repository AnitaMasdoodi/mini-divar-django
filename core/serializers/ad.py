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
            raise serializers.ValidationError('title must contains alphabet')
        return data
