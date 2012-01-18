from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField(blank=True)
    timestamp = models.DateTimeField(blank=True, default=datetime.datetime.now)
