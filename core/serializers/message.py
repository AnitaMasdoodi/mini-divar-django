from rest_framework import serializers
from core.models import Message

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.id')

    class Meta:
        model = Message
        fields = ['id', 'sender', 'text', 'created_at', 'updated_at', 'is_read']