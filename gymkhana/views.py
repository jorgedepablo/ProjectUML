from os import terminal_size
from django import template
from django.shortcuts import render, HttpResponse
from django.http import Http404
from django.template import Template, Context
from gymkhana.utils import *
from .models import *
from ProjectUML.settings import TEMPLATES
# Create your views here.

_ = lambda s: s

def start(request): 
    games = Games.objects.all() # lista con todos los games 

    doc = open(str(TEMPLATES[0]['DIRS'])[2:-2] + "start.html")
    plt = Template(doc.read())
    doc.close()

    ctx=Context({"games_list":games})
    templ = plt.render(ctx)
    return HttpResponse(templ)


def challenge(request):
    game_id = request.GET['game_id']
    last_challenge = int(request.GET['last_challenge'])
    challenge_id = challenge_manager(game_id, last_challenge)
    # challenge_id = request.GET['game']

    try: 
        challenge = Challenges.objects.get(id=challenge_id)
    except Challenges.DoesNotExist:
        raise Http404("No existe")

    #esto lo podriamos manejar para que sea resistente a errores
    challenge_type = Diagrams.objects.get(id=challenge.diagram_type_id)
    challege_title = _(challenge.name)
    challenge_question = _(challenge.question)
    challenge_diagram = challenge.diagram
    challenge_type_name= _(challenge_type.type) 
    challenge_type_description = _(challenge_type.description)


    doc = open(str(TEMPLATES[0]['DIRS'])[2:-2] + "challenge.html")
    plt = Template(doc.read())
    doc.close()
    ctx=Context({"challenge_id":challenge_id,
                "challenge_title":challege_title, 
                "challenge_question":challenge_question, 
                "challenge_diagram":challenge_diagram,
                "challenge_type_name":challenge_type_name,
                "challenge_type_description":challenge_type_description,
                "last_challenge_id":last_challenge,
                "game_id":game_id})

    templ = plt.render(ctx)
    return HttpResponse(templ)


def response(request): 
    lang = request.LANGUAGE_CODE
    challenge_id = request.GET['challenge']
    keyword = request.GET['keyword']
    game_id = request.GET['game_id']
    last_challenge_id = request.GET['last_challenge_id']

    challenge = Challenges.objects.get(id=challenge_id)
    challenges_list = list(Games.objects.get(id=game_id).challenges.all())
    is_last_challenge = True 
    if len(challenges_list) > 1: 
        # es importante que no hay una lista de challenges con el challenge repretido 
        index = challenges_list.index(challenge)
        if index < (len(challenges_list) - 1): 
            is_last_challenge = False

    key = _(challenge.awnser)
    keyword = trans_keyword(keyword, lang)
    template = check_response(key, keyword)

    doc = open(str(TEMPLATES[0]['DIRS'])[2:-2] + template)
    plt = Template(doc.read())
    doc.close()

    ctx=Context({"challenge_id":challenge_id,
                "is_last_challenge":is_last_challenge,
                "last_challenge":last_challenge_id,
                "game_id":game_id})
    templ = plt.render(ctx)
    return HttpResponse(templ)


