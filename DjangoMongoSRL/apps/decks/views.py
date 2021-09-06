from django.shortcuts import render
from rest_framework import viewsets
from .models import Deck
from .serializers import DeckSerializer

# Create your views here.

class DecksViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing car.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer