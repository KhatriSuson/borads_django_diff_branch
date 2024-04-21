from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=230, unique=True)
    description = models.CharField(max_length=239)

    def __str__(self):
        return self.name
    

class Topic(models.Model):
    subject = models.CharField(max_length=355)
    last_update = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)


class Post(models.Model):
    message = models.TextField(max_length = 49999)
    topic = models.ForeignKey(Topic, related_name="topics", on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name = 'posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null = True, related_name = '+', on_delete=models.CASCADE)
    

