from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('categories/', include('api.endpoints.category', namespace='category')),
    path('ads/', include('api.endpoints.ad', namespace='ad')),
    path('cities/', include('api.endpoints.city', namespace='city')),
    path('conversations/', include('api.endpoints.conversation', namespace='conversation')),
    path('messages/', include('api.endpoints.message', namespace='message')),
    path('my-ads/', include('api.endpoints.my_ads', namespace='my_ads')),
    path('swagger/', include('api.endpoints.swagger')),
]