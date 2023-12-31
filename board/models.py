from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=150)
    discribtion = models.CharField(max_length=250)

    def __str__(self) :
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=5000)
    created_by = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board,related_name='topic', on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField()
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic,related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.message

