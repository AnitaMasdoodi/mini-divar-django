from rest_framework import generics, permissions
from core.models import Conversation
from core.serializers.conversation import ConversationSerializer
from django.db.models import Q

class ConversationListCreateView(generics.ListCreateAPIView):
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Conversation.objects.filter(Q(buyer=user) | Q(seller=user))

    def perform_create(self, serializer):
        ad = serializer.validated_data['ad']
        serializer.save(
            buyer=self.request.user,
            seller=ad.user
        )

class ConversationDetailView(generics.RetrieveAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Conversation.objects.filter(buyer=user) | Conversation.objects.filter(seller=user)