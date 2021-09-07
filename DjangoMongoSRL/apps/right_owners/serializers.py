from rest_framework import serializers
from .models import RightOwner


class RightOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RightOwner
        fields = ['name', 'role', 'ipi']