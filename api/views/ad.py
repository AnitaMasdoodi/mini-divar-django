from django.core.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from core.models import Ad
from core.serializers import AdSerializer
from core.pagination import Paginator


class AdListCreateApiView(ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = Paginator
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Ad.objects.all()
        return Ad.objects.all()

    def perform_update(self, serializer):
        if serializer.instance.user != self.request.user:
            raise PermissionDenied("You can't edit this ad.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("You can't delete this ad.")
        instance.delete()


class MyAdsListApiView(ListAPIView):
    serializer_class = AdSerializer
    pagination_class = Paginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ad.objects.filter(user=self.request.user)