from django.db import models

# Create your models here.

class Descriptions(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
