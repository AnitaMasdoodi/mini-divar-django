from django.urls import path
from api.views import MessageListCreateView

app_name = 'message'
urlpatterns = [
    path('<uuid:conversation_id>/', MessageListCreateView.as_view(), name='message-list'),
]