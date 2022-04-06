from os import terminal_size
from django import template
from django.shortcuts import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.template import Template, Context, loader
from django.shortcuts import render
from gymkhana.utils import *
from .models import *
from ProjectUML.settings import TEMPLATES
# Create your views here.

_ = lambda s: s

def start(request): 
    try: 
        games = Games.objects.all() # lista con todos los games 
    except Games.DoesNotExist:
        raise Http404("No existe")
    plt = loader.get_template('start.html')
    templ = plt.render({"games_list":games})

    return HttpResponse(templ)


def profile(request):
    app_user_name = None
    app_user_points = None
    if str(request.user) != 'AnonymousUser': 
        user = request.user
        user_is_registered = check_new_user(user)
        if user_is_registered == False:
            register_user(user)
    app_user_name, app_user_points = get_user_info(user)
    plt = loader.get_template('profile.html')
    templ = plt.render({"user_name": app_user_name,
                        "user_points": app_user_points})

    return HttpResponse(templ)


def create_challenge(request):
    if request.method == 'POST':
        form = request.POST
        print(form)
        #if form.is_valid():
        #   form.save()
        return HttpResponseRedirect('/profile/')

    if str(request.user) != 'AnonymousUser': 
        user = request.user
        user_is_registered = check_new_user(user)
        if user_is_registered == False:
            return HttpResponse("You must register first")
        app_user_name, app_user_points = get_user_info(user)
        diagrams_list = Diagrams.objects.all()
        data = {'diagrams_list':diagrams_list,
                'user_name': app_user_name,
                'user_points': app_user_points, 
                'csrf_token':request.COOKIES['csrftoken']}
        plt = loader.get_template('create_challenge.html')
        print(app_user_name)
        templ = plt.render(data)
        return HttpResponse(templ)
    else:
        return HttpResponse("You must register first")


def create_game(request):
    if str(request.user) != 'AnonymousUser': 
        user = request.user
        user_is_registered = check_new_user(user)
        if user_is_registered == False:
            return HttpResponse("You must register first")
        app_user_name, app_user_points = get_user_info(user)
        challenges_list = Challenges.objects.all()
        data = {'challenges_list':challenges_list,
                'user_name': app_user_name,
                'user_points': app_user_points, 
                'csrf_token':request.COOKIES['csrftoken']}
        plt = loader.get_template('create_game.html')
        print(app_user_name)
        templ = plt.render(data)
        return HttpResponse(templ)
    else:
        return HttpResponse("You must register first")


def challenge(request):
    game_id = request.GET['game_id']
    last_challenge = int(request.GET['last_challenge'])
    challenge_id = challenge_manager(game_id, last_challenge)

    try: 
        challenge = Challenges.objects.get(id=challenge_id)
    except Challenges.DoesNotExist:
        raise Http404("No existe")

    # esto lo podriamos manejar para que sea resistente a errores
    challenge_type = Diagrams.objects.get(id=challenge.diagram_type_id)
    challege_title = _(challenge.name)
    challenge_question = _(challenge.question)
    challenge_diagram = challenge.diagram
    challenge_type_name= _(challenge_type.type) 
    challenge_type_description = _(challenge_type.description)

    plt = loader.get_template('challenge.html')
    templ = plt.render({"challenge_id":challenge_id,
                "challenge_title":challege_title, 
                "challenge_question":challenge_question, 
                "challenge_diagram":challenge_diagram,
                "challenge_type_name":challenge_type_name,
                "challenge_type_description":challenge_type_description,
                "last_challenge_id":last_challenge,
                "game_id":game_id})

    return HttpResponse(templ)


def response(request): 
    lang = request.LANGUAGE_CODE
    user = request.user
    challenge_id = request.GET['challenge']
    keyword = request.GET['keyword']
    game_id = request.GET['game_id']
    last_challenge_id = request.GET['last_challenge_id']
    try: 
        challenge = Challenges.objects.get(id=challenge_id)
    except Challenges.DoesNotExist:
        raise Http404("No existe")

    challenges_list = list(Games.objects.get(id=game_id).challenges.all())
    is_last_challenge = True 
    if len(challenges_list) > 1:
        index = challenges_list.index(challenge)
        if index < (len(challenges_list) - 1): 
            is_last_challenge = False

    key = _(challenge.awnser)
    keyword = trans_keyword(keyword, lang)
    is_correct = check_response(key, keyword)
    if is_correct: 
        template = 'success.html'
        increase_user_points(user, challenge)
    else:
        template = 'wrong.html'
    app_user_name, app_user_points = get_user_info(user)

    plt = loader.get_template(template)
    templ = plt.render({"challenge_id":challenge_id,
                "is_last_challenge":is_last_challenge,
                "last_challenge":last_challenge_id,
                "user_name":app_user_name,
                "user_points":app_user_points,
                "game_id":game_id})

    return HttpResponse(templ)

