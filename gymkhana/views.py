from django import template
from django.shortcuts import render, HttpResponse
from django.http import Http404
from django.template import Template, Context
from gymkhana.utils import check_response, trans_keyword
from .models import *
from ProjectUML.settings import TEMPLATES
# Create your views here.

_ = lambda s: s

def start(request): 
    return render(request, 'start.html')


def game(request): 
    challenge_id = request.GET['game']
    try: 
        challenge = Challenges.objects.get(id=challenge_id)
    except Challenges.DoesNotExist: 
        raise Http404("No existe")

    #esto lo podriamos manejar para que sea resistente a errores
    #challenge_type = Diagrams.objects.get(name=challenge.diagram_type)
    challege_title = _(challenge.title)
    challenge_question = _(challenge.question)
    challenge_diagram = challenge.diagram
    #challenge_type_name= challenge_type.name 
    #challenge_type_description = challenge_type.description


    doc = open(str(TEMPLATES[0]['DIRS'])[2:-2] + "game.html")
    plt = Template(doc.read())
    doc.close()
    ctx=Context({"challenge_id":challenge_id,
                 "challenge_title":challege_title, 
                 "challenge_question":challenge_question, 
                 "challenge_diagram":challenge_diagram})
                 #"challenge_type_name":challenge_type_name,
                 #"challenge_type_description":challenge_type_description})

    template = plt.render(ctx)

    return HttpResponse(template)
    #return render(request, template)


def response(request): 
    lang = request.LANGUAGE_CODE
    challenge_id = request.GET['challenge']
    keyword = request.GET['keyword']

    challenge = Challenges.objects.get(id=challenge_id)
    key = _(challenge.awnser)

    keyword = trans_keyword(keyword, lang)
    template = check_response(key, keyword)

    return render(request, template)
