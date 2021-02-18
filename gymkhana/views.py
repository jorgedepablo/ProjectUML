from django.shortcuts import render, HttpResponse 

# Create your views here.

def start(request): 

    return HttpResponse('Init the gymkhana app...')

def quest(request): 

    return render(request, "first_question.html")

def response(request): 

    msg = "First challenge complete !  %r " %request.GET["surname"]

    return HttpResponse(msg)