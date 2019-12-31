from django.db import models
from django.utils import timezone

# Create your models here.
class Word(models.Model):
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
