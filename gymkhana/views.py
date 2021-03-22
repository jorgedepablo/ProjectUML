from django.shortcuts import render, HttpResponse 
from gymkhana.utils import check_response
# Create your views here.

def start(request): 

    return render(request, 'start.html')


def game_1(request): 
    # diagrama de actividades
    return render(request, 'game_1.html')

def game_2(request): 
    # Diagrama de casos de uso
    return render(request, 'game_2.html')

def game_3(request): 
    #  Object Diagrams
    return render(request, 'game_3.html')


def response_1(request): 

    key = 'nal hutta'
    keyword = request.GET['keyword']
    template = check_response(key, keyword)

    return render(request, template)

def response_2(request): 

    key = 'fight zombies'
    keyword = request.GET['keyword']
    template = check_response(key, keyword)

    return render(request, template)

def response_3(request): 

    key = 'no humans'
    keyword = request.GET['keyword']
    template = check_response(key, keyword)

    return render(request, template)