from rest_framework import serializers
from .models import Music, Title
from apps.right_owners.serializers import RightOwnerSerializer


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['title', 'type']


class MusicSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(source='id_society')
    titles = TitleSerializer(many=True, read_only=True, source='title_music')
    right_owner = RightOwnerSerializer(many=True, read_only=True)
    class Meta:
        model = Music
        fields = ['_id', 'iswc', 'titles', 'right_owner']