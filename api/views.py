from django.shortcuts import render
from rest_framework import viewsets
from pokedex.models import Pokemon, Trainer
from .serializers import PokemonSerializer, TrainerSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from oauth2_provider.contrib.rest_framework import TokenHasScope

class PokemonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pokemons to be viewed or edited.
    """
    queryset = Pokemon.objects.all().order_by('name')
    serializer_class = PokemonSerializer
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticatedOrReadOnly()]
        return []

class TrainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trainers to be viewed or edited.
    """
    queryset = Trainer.objects.all().order_by('nombre')
    serializer_class = TrainerSerializer
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticatedOrReadOnly()]
        return []