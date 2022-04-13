from django.db import models
from django.db.models.fields import DurationField, EmailField
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.db.models.signals import ModelSignal

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    admin = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    challenges_passed = models.ManyToManyField('Challenges', blank=True)
    created_at = models.DateTimeField(null=True, default=None)
    updated_at = models.DateTimeField(null=True, default=None)

class Diagrams(models.Model): 
    name = models.CharField(max_length=100) # cambiar por name en la próxima actualización de
    description = models.CharField(max_length=10000)

class Challenges(models.Model): 
    name = models.CharField(max_length=50) 
    question = models.CharField(max_length=10000)
    answer = models.CharField(max_length=100)
    diagram = models.CharField(max_length=20) 
    image = models.ImageField(upload_to=('challenges/'), null=True, blank=True)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE, default="")
    diagram_type = models.ForeignKey(Diagrams, on_delete=models.CASCADE, default="")
    created_at = models.DateTimeField(null=True, default=None)
    points = models.IntegerField(default=0)

class Games(models.Model): 
    title = models.CharField(max_length=50)
    challenges = models.ManyToManyField(Challenges)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE, default="")
    created_at = models.DateTimeField(null=True, default=None)


