from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField()
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User)
