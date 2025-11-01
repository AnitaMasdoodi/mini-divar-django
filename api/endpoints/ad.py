from django.urls import path
from api.views import AdListCreateApiView, AdDetailApiView

app_name = 'ad'
urlpatterns = [
    path('', AdListCreateApiView.as_view(), name='ad-list-create'),
    path('<slug:slug>/', AdDetailApiView.as_view(), name='ad-detail'),
]
