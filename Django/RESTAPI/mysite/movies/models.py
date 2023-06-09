from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
class Moviedata(models.Model):
    def __str__(self):
        return self.name
    
    name=models.CharField(max_length=200)
    duration=models.FloatField()
    rating=models.FloatField()
    typ=models.CharField(max_length=200, default='action')
    image=models.ImageField(upload_to='Images/',default="Images/None/Noimg.jpg")
