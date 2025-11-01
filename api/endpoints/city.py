from django.urls import path
from api.views import CityDetailApiView, CityListCreateApiView

app_name = 'city'
urlpatterns = [
    path('', CityListCreateApiView.as_view(), name='city-list-create'),
    path('<uuid:pk>/', CityDetailApiView.as_view(), name='city-detail'),
]