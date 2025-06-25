from django.shortcuts import render
from rest_framework import viewsets
from pokedex.models import Pokemon, Trainer
from .serializers import PokemonSerializer, TrainerSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pokemons to be viewed or edited.
    """
    queryset = Pokemon.objects.all().order_by('name')
    serializer_class = PokemonSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trainers to be viewed or edited.
    """
    queryset = Trainer.objects.all().order_by('nombre')
    serializer_class = TrainerSerializer