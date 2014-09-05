from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime


class Message(models.Model):
    """
    A message is related to a user
    """

    user = models.ForeignKey(User)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    content = models.CharField(max_length=160)
    date = models.DateTimeField(auto_now=True, default=datetime.now())

    def __unicode__(self):
        return "<Message {} {} {} (User id {})>".format(self.source, self.destination, self.content, self.user_id)

    def subject(self):
        """
        First 15 chars are the message subject
        """
        return self.content[:15]