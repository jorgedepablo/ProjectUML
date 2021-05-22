from django.db import models
from django.db.models.fields import EmailField
from django.db.models.signals import ModelSignal

# Create your models here.

class Challenge(models.Model): 
    question = models.CharField()
    awnser = models.CharField(max_length=100)
    diagram = models.CharField(max_length=20) # el path del repo donde esté el diagrama 

class Game(models.Model): 
    title = models.CharField(max_length=50)
    description = models.CharField()
    challenge = models.ManyToManyField(Challenge)

class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    score = models.IntegerField() # posible desarrollo para que tengas puntos por resolver challenges