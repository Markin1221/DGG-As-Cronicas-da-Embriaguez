from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import CharacterViewSet, ItemViewSet, DrinkViewSet

router = DefaultRouter()
router.register(r'personagens', CharacterViewSet)
router.register(r'itens', ItemViewSet)
router.register(r'bebidas', DrinkViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),           # ViewSets que precisam de crud automatico
    path('api/', include('core.urls')),           # outras views como ataque que tem que ser manuais
]
