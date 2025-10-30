from django.urls import path
from .views import UserListApiView, RegisterApiView,UserDetailApiView, UserAdminDetailApiView

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('me/', UserDetailApiView.as_view(), name='user-detail'),
    path('users/', UserListApiView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserAdminDetailApiView.as_view(), name='user-admin-detail'),
]