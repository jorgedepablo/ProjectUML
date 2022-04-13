from os import terminal_size
from datetime import datetime
from django import template
from django.shortcuts import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.template import Template, Context, loader
from django.shortcuts import render
from gymkhana.utils import *
from .models import *
from .forms import *
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
    if str(request.user) != 'AnonymousUser': 
        user = request.user
        user_is_registered = check_new_user(user)
        if user_is_registered == False:
            return HttpResponse("You must register first")

        data = {'diagrams_list':Diagrams.objects.all(),
                'user_name': get_user_info(user)[0],
                'csrf_token':request.COOKIES['csrftoken']}
        plt = loader.get_template('create_challenge.html')
        templ = plt.render(data)
        return HttpResponse(templ)
    else:
        return HttpResponse("You must register first")

def upload_challenge(request):
    if str(request.user) != 'AnonymousUser': 
        if request.method == 'POST':
            print(request.FILES)
            form = ChallengeForm(request.POST, request.FILES)
            if form.is_valid():
                print("Holaaaaa")
                challenge = Challenges()
                challenge.name = form.cleaned_data['name']
                challenge.question = form.cleaned_data['question']
                challenge.answer = form.cleaned_data['answer']
                challenge.diagram = "dummy texttt QUITARR"
                challenge.image = form.cleaned_data['image']
                challenge.creator = Users.objects.get(email=request.user.email)
                challenge.diagram_type = form.cleaned_data['diagram_type']
                challenge.points = form.cleaned_data['points']
                challenge.created_at = datetime.now()
                challenge.save()
                return HttpResponseRedirect('/profile/')
            else: 
                print(form.errors)
                return HttpResponse("Something went wrong")
        else:
            return HttpResponse("Something went wrong")
    else: 
        return HttpResponse("You must register first")

def create_game(request):
    if str(request.user) != 'AnonymousUser': 
        user = request.user
        user_is_registered = check_new_user(user)
        if user_is_registered == False:
            return HttpResponse("You must register first")
        data = {'challenges':Challenges.objects.all(),
                'user_name': get_user_info(user)[0],
                'csrf_token':request.COOKIES['csrftoken']}
        plt = loader.get_template('create_game.html')
        templ = plt.render(data)
        return HttpResponse(templ)
    else:
        return HttpResponse("You must register first")

def upload_game(request):
    if str(request.user) != 'AnonymousUser': 
        if request.method == 'POST':
            form = GameForm(request.POST, request.FILES)
            if form.is_valid():
                game = Games()
                game.creator = Users.objects.get(email=request.user.email)
                game.title = form.cleaned_data['title']
                game.created_at = datetime.now()
                game.save() # it must exist before ManyToMany field
                game.challenges.set(form.cleaned_data['challenges'])
                game.save()
            return HttpResponseRedirect('/profile/')
        else: 
            return HttpResponse("Something went wrong")
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

    diagram_type = Diagrams.objects.get(id=challenge.diagram_type_id)
    diagram_type_name = _(diagram_type.diagram_type) # cambiar a name en la próxima actualizaci´´on de models
    diagram_type_description = _(diagram_type.description)

    data = {"challenge_id":challenge_id,
            "challenge_title":challenge.name, 
            "challenge_question":challenge.question, 
            "challenge_image":challenge.image,
            "diagram_name":diagram_type_name,
            "diagram_description": diagram_type_description,
            "points":challenge.points,
            "last_challenge_id":last_challenge,
            "game_id":game_id}

    plt = loader.get_template('challenge.html')
    templ = plt.render(data)

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

    key = _(challenge.answer)
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

