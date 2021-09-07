from rest_framework import viewsets
from .models import RightOwner
from .serializers import RightOwnerSerializer


class RightOwnersViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing RightOwner.
    """
    queryset = RightOwner.objects.all()
    serializer_class = RightOwnerSerializer