from django.http import HttpResponse
from django.shortcuts import render, HttpResponse 

def index(request):

    return render(request, 'home.html')
