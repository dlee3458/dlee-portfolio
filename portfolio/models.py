from django.db import models
from django.utils import timezone

class Message(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.TextField(blank=True)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email