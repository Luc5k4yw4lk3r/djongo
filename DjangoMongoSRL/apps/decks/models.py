from django.db import models

# Create your models here.
class Deck(models.Model):
    name = models.TextField(help_text="Deck name")

    def __str__(self) -> str:
        return self.name