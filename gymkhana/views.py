from django.shortcuts import render, HttpResponse 

# Create your views here.

def start(request): 

    return render(request, 'start.html')


def quest_1(request): 

    return render(request, 'first_question.html')

def quest_2(request): 

    return render(request, 'first_question.html')

def quest_3(request): 

    return render(request, 'first_question.html')


def response_1(request): 

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

def response_3(request): 

    key = 'De Pablo'

    if str(request.GET['surname']) != key: 
        msg = 'The surname %s is not good enough' %request.GET['surname']
    else:
        msg = 'The best surname ever, Mr. %s' %request.GET['surname']

    return HttpResponse(msg)