from django.urls import path
from api.views import MyAdsListApiView

app_name = 'my_ads'
urlpatterns = [
    path('', MyAdsListApiView.as_view(), name='my_ads'),
]