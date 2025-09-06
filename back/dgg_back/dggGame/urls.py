from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import PersonagemViewSet, ItemViewSet, BebidaViewSet
urlpatterns = [
    path('admin/', admin.site.urls),
]


router = DefaultRouter()
router.register(r'personagens', PersonagemViewSet)
router.register(r'itens', ItemViewSet)
router.register(r'bebidas', BebidaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
