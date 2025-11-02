from rest_framework import serializers
from core.models import Conversation, Ad
from core.serializers.message import MessageSerializer

class ConversationSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.id')
    seller = serializers.ReadOnlyField(source='seller.id')
    ad = serializers.PrimaryKeyRelatedField(queryset=Ad.objects.all())
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'ad', 'buyer', 'seller', 'created_at', 'updated_at', 'messages']