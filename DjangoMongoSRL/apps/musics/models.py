from django.db import models
from apps.right_owners.models import RightOwner
#from apps.decks.models import RightOwners


SOURCE_TYPES = (
    ('original_title', 'ORIGINAL TITLE'),
    ('alternative_title_1', 'ALTERNATIVE TITLE 1'),
    ('alternative_title_2', 'ALTERNATIVE TITLE 2'),
    ('alternative_title_3', 'ALTERNATIVE TITLE 3'),
    ('alternative_title_4', 'ALTERNATIVE TITLE 4')
)


class Music(models.Model):
    _id = models.CharField(max_length=100, help_text="Internal work id assigned by the society that provided the file.")
    iswc = models.CharField(max_length=100, help_text="International Standard Musical Work Code")
    right_owner = models.ManyToManyField(RightOwner)
    
    def __str__(self) -> str:
        return 'Id Society: {} ISWC: {}'.format(self._id, self.iswc)


class Title(models.Model):
    title = models.CharField(max_length=200, help_text="Title", null=False)
    type = models.CharField(choices=SOURCE_TYPES, max_length=200, null=True, blank=True, help_text='Title type')
    music = models.ForeignKey(Music, on_delete=models.PROTECT, related_name='title_music')

    def __str__(self) -> str:
        return 'Title: {}'.format(self.title)
