from django.db import models
from django.db.models.fields import DurationField, EmailField
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.db.models.signals import ModelSignal

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    admin = models.BooleanField()

class Diagrams(models.Model): 
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)

class Challenges(models.Model): 
    #diagram_type = models.ForeignKey(Diagrams)
    name = models.CharField(max_length=50)
    question = models.CharField(max_length=10000)
    awnser = models.CharField(max_length=100)
    diagram = models.CharField(max_length=20) 
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)
    diagram_type = models.ForeignKey(Diagrams, on_delete=models.CASCADE)

class Games(models.Model): 
    title = models.CharField(max_length=50)
    challenges = models.ManyToManyField(Challenges)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)


