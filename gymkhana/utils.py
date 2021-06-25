"""
Script that contents some functions for Gymkhana App extern to Django.

"""
import os 
from ProjectUML.settings import BASE_DIR
from .models import *
import polib #RECORDAR METER EN EL REQUIREMENTS DE HEROKU!!!!

def challenge_manager(game, last_challenge): 
    """Retrun the next challenge into a challenges list linked with specified game list. """
    challenges_list = list(Games.objects.get(id=game).challenges.all())
    if last_challenge != 0: 
        i = 0 
        while True: 
            if int(challenges_list[i].id) != last_challenge: 
                i += 1 
            else:
                # es importante que no se meta aqui si es el último de la lista
                # en caso de que fuera el último juego de la lista last_challenge no deberñia volver aquí
                challenge_id = challenges_list[i+1].id
                break
    else: 
        challenge_id = challenges_list[0].id

    return challenge_id 

def check_response(key, keyword): 
    keyword = str(keyword).lower()
    if keyword != key: 
        template = 'wrong.html'
    else:
        template = 'success.html'
    return template

def trans_keyword(keyword, lang): 
    """ Reverse translate the keywords to have them in English."""
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

