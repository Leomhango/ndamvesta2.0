from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=255, unique=True)
    pos = models.CharField(max_length=255)
    description = models.TextField()
    inSentence = models.TextField()

    def __str__(self):
        return self.word