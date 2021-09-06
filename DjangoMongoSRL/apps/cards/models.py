from django.db import models
from apps.decks.models import Deck

# Create your models here.
class Card(models.Model):
    question = models.TextField(help_text="Card name")
    answer = models.TextField(help_text="Card name")
    value = models.IntegerField(help_text="Number of card", blank=True, null=True)

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.question