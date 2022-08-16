from django.db import models

# Create your models here.

class Games(models.Model):
    name = models.CharField(max_length=255)
    description =models.TextField()
    year = models.DateField()

    def __str__(self) -> str:
        return self.name, self.description, self.year