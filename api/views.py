from django.shortcuts import render
from .models import Games
from .serializers import GamesSerializers
from rest_framework import viewsets

# Create your views here.

class GamesViewset(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializers


