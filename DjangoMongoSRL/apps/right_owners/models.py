from django.db import models

# Create your models here.
class RightOwner(models.Model):
    name = models.CharField(max_length=200, help_text="Right Owner's name", null=False)
    role = models.CharField(max_length=200, help_text="Right Owner's role", null=False)
    ipi = models.CharField(max_length=200, help_text="International identification number assigned to the right owner.", null=False)

    def __str__(self) -> str:
        return self.name