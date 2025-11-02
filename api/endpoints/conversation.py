from django.urls import path
from api.views import ConversationListCreateView, ConversationDetailView

app_name = 'conversation'
urlpatterns = [
    path('', ConversationListCreateView.as_view(), name='conversation-list'),
    path('<uuid:pk>/', ConversationDetailView.as_view(), name='conversation-detail'),
]