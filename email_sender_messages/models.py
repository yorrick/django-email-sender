from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """
    A message is related to a user
    """

    user = models.ForeignKey(User)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    content = models.CharField(max_length=160)
