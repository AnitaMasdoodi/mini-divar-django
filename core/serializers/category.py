from rest_framework import serializers
from core.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'created_at', 'updated_at']

    def validate_title(self, data: str):
        if data.isnumeric():
            raise serializers.ValidationError('Title must contain alphabet')
        elif len(data) < 2:
            raise serializers.ValidationError('Title must contain at least two letters')
        return data