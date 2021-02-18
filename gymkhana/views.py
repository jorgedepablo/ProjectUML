from django.shortcuts import render, HttpResponse 

# Create your views here.

def start(request): 

    return HttpResponse('Init the gymkhana app...')


def quest(request): 

    return render(request, 'first_question.html')


def response(request): 

    key = 'De Pablo'

    if  str(request.GET['surname']) != key: 
        msg = 'The surname %s is not good enough' %request.GET['surname']
    else: 
        msg = 'The best surname ever, Mr. %s' %request.GET['surname']

    return HttpResponse(msg)