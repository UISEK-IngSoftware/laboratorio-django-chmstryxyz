from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet, TrainerViewSet

router = DefaultRouter()
router.register(r'pokemons', PokemonViewSet, basename='pokemon')
router.register(r'trainers', TrainerViewSet, basename='trainer')

urlpatterns = [
    path('', include(router.urls)),
]