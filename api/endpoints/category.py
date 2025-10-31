from django.urls import path
from api.views import CategoryListCreateApiView, CategoryDetailApiView

app_name = 'category'
urlpatterns = [
    path('', CategoryListCreateApiView.as_view(), name='category-list-create'),
    path('<uuid:pk>/', CategoryDetailApiView.as_view(), name='category-detail'),
]