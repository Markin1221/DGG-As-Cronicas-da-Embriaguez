from django.urls import path
from .views import ataqueViewSet

urlpatterns = [
    path('ataque/', ataqueViewSet.as_view(), name='ataque'),
]
