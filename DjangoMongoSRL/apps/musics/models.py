from django.db import models
#from apps.decks.models import RightOwners

# Create your models here.
class Music(models.Model):
    _id = models.CharField(max_length=100, help_text="Internal work id assigned by the society that provided the file.")
    iswc = models.CharField(max_length=100, help_text="International Standard Musical Work Code")
    original_title = models.CharField(max_length=200, help_text="Original Title", null=False)
    alternative_title_1 = models.CharField(max_length=200, blank=True, null=False, help_text="Alternative Title 1")
    alternative_title_2 = models.CharField(max_length=200, blank=True, null=False, help_text="Alternative Title 2")
    # right_owners = models.ManyToOneRel(RightOwners, on_delete=models.CASCADE, help_text="Agents who have rights over the musical work (composers,publishers…).")
    alternative_title_3 = models.CharField(max_length=200, blank=True, null=False, help_text="Alternative Title 3")

    def __str__(self) -> str:
        return 'Id Society: {} ISWC: {}'.format(self._id, self.iswc)