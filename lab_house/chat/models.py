
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Room(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)


class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)