from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Posts(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Create_date = models.DateTimeField()
    Published_date = models.DateTimeField()
