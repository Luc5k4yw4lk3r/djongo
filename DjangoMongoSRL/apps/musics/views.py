from rest_framework import viewsets
from .models import Music, Title
from .serializers import MusicSerializer, TitleSerializer


class MusicsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing car.
    """
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class TitlesViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing car.
    """
    queryset = Title.objects.all()
    serializer_class = TitleSerializer