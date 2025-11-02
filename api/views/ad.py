from django.core.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from core.models import Ad
from core.serializers import AdSerializer
from core.pagination import Paginator


class AdListCreateApiView(ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = Paginator
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'city']
    search_fields = ['title']
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

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