"""
Script that contents some functions for Gymkhana App extern to Django.

"""
import os 
from ProjectUML.settings import BASE_DIR
from .models import *
import polib #RECORDAR METER EN EL REQUIREMENTS DE HEROKU!!!!
import time


def check_new_user(user): 
    """Check if a user registered by django.auth is on app database."""
    user_is_registered = False
    if user != None: 
        django_user = user 
        app_users = list(Users.objects.all())
        i = 0 
        while i <= len(app_users): 
            if django_user.email != app_users[i].email:
                i += 1 
            else: 
                user_is_registered = True 
                break 
    return user_is_registered

def register_user(user): 
    """Register a user form django.auth in the app database."""
    if user != None: 
        app_user = Users(name=user.name, 
                        email=user.email, 
                        admin=user.is_superuser, 
                        points=0)
        app_user.save()

def get_user_info(request_user):
    """Get the user information from the app database in tuple form (name, points)."""
    app_user_name = None
    app_user_points = None
    if str(request_user) != 'AnonymousUser': 
        user = request_user
        user_is_registered = check_new_user(user)
        if user_is_registered != False:
            app_user = Users.objects.get(email=user.email)
            app_user_name = app_user.name
            app_user_points = app_user.points
    return (app_user_name, app_user_points)

def increase_user_points(request_user, challenge):
    """Increase the user points if he/she does not alredy passed it and saved in the app database."""
    challenge_points = 10
    if str(request_user) != 'AnonymousUser': # this feature is just for registred users
        user = request_user
        user_is_registered = check_new_user(user)
        if user_is_registered != False:
            app_user = Users.objects.get(email=request_user.email)
            if challenge.points > 0 and challenge.points != None: 
                challenge_points = challenge.points
            challenges_passed = app_user.challenges_passed.all()
            if challenge not in challenges_passed:
                app_user.points += challenge_points
                app_user.challenges_passed.add(challenge)
                app_user.save()

def challenge_manager(game, last_challenge): 
    """Retrun the next challenge into a challenges list linked with specified game list. """
    challenges_list = list(Games.objects.get(id=game).challenges.all())
    if last_challenge != 0: 
        i = 0 
        while True: 
            if int(challenges_list[i].id) != last_challenge: 
                i += 1 
            else:
                challenge_id = challenges_list[i+1].id
                break
    else: 
        challenge_id = challenges_list[0].id
    return challenge_id 

def check_response(key, keyword):
    """Check if response are correct and returns the template view for the user."""
    keyword = str(keyword).lower()
    if keyword != key: 
        correct = False
    else:
        correct = True
    return correct

def check_last_challenge(game, challenge):
    """Check if the challenge is the last challenge of the game."""
    last_challenge = True
    challenges = list(Games.objects.get(id=game).challenges.all())
    if len(challenges) > 1: 
        if int(challenges[-1].id) != int(challenge): 
            last_challenge = False
    return last_challenge

def trans_keyword(keyword, lang): 
    """Reverse translate the keywords to have them in English."""
    keyword = str(keyword).lower()
    key_translated = keyword

    if (lang != 'en' ): 
        locale_file = os.path.join(BASE_DIR, "locale", lang, "LC_MESSAGES", "django.po")
        po = polib.pofile(locale_file)
        i = 0 
        while i < len(po):
            if po[i].msgstr != keyword: 
                pass
            else: 
                key_translated = po[i].msgid
                break
            i += 1
    return key_translated

# def upload_challenge(form, creator): 
#     """Upload a challenge to the database."""
#     # parser the form data
#     title = form.cleaned_data['title'] 
#     description = form.cleaned_data['description']
#     points = form.cleaned_data['points']
#     keyword = form.cleaned_data['keyword']
#     challenge = Challenges.objects.filter(title=title)

#     if challenge.count() == 0:
#         challenge = Challenges(title=title, 
#                                 description=description, 
#                                 points=points, 
#                                 keyword=keyword, 
#                                 creator=creator)
#         challenge.save()
