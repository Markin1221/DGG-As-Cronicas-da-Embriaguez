from django.urls import path
from .views import ataqueViewSet

ataque_list = ataqueViewSet.as_view({'get': 'list', 'post': 'create'})
ataque_detail = ataqueViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

urlpatterns = [
    path('ataque/', ataque_list, name='ataque-list'),
    path('ataque/<int:pk>/', ataque_detail, name='ataque-detail'),
]
