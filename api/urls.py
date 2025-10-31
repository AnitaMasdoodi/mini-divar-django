from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('categories/', include('api.endpoints.category', namespace='category')),
]