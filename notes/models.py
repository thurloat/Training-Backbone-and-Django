from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=140)
    completed = models.BooleanField(default=True)
