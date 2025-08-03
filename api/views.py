from django.shortcuts import render
from rest_framework import viewsets
from pokedex.models import Pokemon, Trainer
from .serializers import PokemonSerializer, TrainerSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all().order_by('name')
    serializer_class = PokemonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all().order_by('nombre')
    serializer_class = TrainerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]