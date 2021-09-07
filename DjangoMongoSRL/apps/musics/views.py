from django.shortcuts import render
from rest_framework import viewsets
from .models import Music, Title
from .serializers import MusicSerializer, TitleSerializer

# Create your views here.

class MusicsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing car.
    """
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]


class TitlesViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing car.
    """
    queryset = Title.objects.all()
    serializer_class = TitleSerializer