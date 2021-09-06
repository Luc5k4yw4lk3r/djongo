from django.shortcuts import render
from rest_framework import viewsets
from .models import Music
from .serializers import MusicSerializer

# Create your views here.

class MusicsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing car.
    """
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]