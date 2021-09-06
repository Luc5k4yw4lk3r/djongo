from django.shortcuts import render
from rest_framework import viewsets
from .models import Card
from .serializers import CardSerializer

# Create your views here.

class CardsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing car.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]