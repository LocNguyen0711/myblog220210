from time import timezone
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class mCreatepost(models.Model):
     title = models.CharField(max_length=200)
     discription = models.TextField()
     body = models.TextField()     
     def __str__(self):
          return f"{self.id}: {self.title} - {self.discription}"
