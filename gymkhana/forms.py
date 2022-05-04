from email.mime import image
from django import forms

from .models import Challenges, Games, Diagrams

class GameForm(forms.ModelForm):
    title = forms.CharField(max_length=50, help_text="Max 50 characters")
    challenges = forms.ModelMultipleChoiceField(queryset=Challenges.objects.all().order_by('id'))
    class Meta:
        model = Games
        fields = ['title', 'challenges']


class ChallengeForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text="Max 50 characters")
    question = forms.CharField(max_length=10000)
    answer = forms.CharField(max_length=100)
    image = forms.ImageField()
    diagram_type = forms.ModelChoiceField(queryset=Diagrams.objects.all())
    points = forms.IntegerField()
    class Meta:
        model = Challenges
        fields = ['name', 'question', 'answer', 'image', 'diagram_type', 'points']