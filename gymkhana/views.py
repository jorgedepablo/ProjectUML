from django.shortcuts import render, HttpResponse 

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

    key = 'Nal Hutta'

    if str(request.GET['keyword']) != key: 
        msg = 'The surname %s is not good enough' %request.GET['surname']
        template = 'wrong.html'
    else:
        msg = 'The best surname ever, Mr. %s' %request.GET['surname']
        # recondicr a success
        template = 'success.html'

    return HttpResponse(msg)

def response_2(request): 

    key = 'De Pablo'

    if str(request.GET['surname']) != key: 
        msg = 'The surname %s is not good enough' %request.GET['surname']
    else:
        msg = 'The best surname ever, Mr. %s' %request.GET['surname']

    return HttpResponse(msg)

def response_3(request): 

    key = 'De Pablo'

    if str(request.GET['surname']) != key: 
        msg = 'The surname %s is not good enough' %request.GET['surname']
    else:
        msg = 'The best surname ever, Mr. %s' %request.GET['surname']

    return HttpResponse(msg)