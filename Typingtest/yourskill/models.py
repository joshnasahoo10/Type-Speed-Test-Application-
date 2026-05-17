from django.db import models
from django.contrib.auth.models import User

class Paragraph(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Score(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    wpm = models.IntegerField()

    accuracy = models.FloatField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username