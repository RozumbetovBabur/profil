from django.db import models

# Create your models here.

class MessageChat(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,null=True)
    teme = models.CharField(max_length=500,null=True)
    message = models.TextField()


