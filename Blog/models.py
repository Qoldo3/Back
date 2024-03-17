from django.db import models


class Post(models.Model):
    Title = models.CharField(max_length=255)
    context = models.TextField()
    abstract = models.TextField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    