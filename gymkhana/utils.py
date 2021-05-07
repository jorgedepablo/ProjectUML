"""
Script that contents some functions for Gymkhana App extern to Django.

"""
import os 
from ProjectUML.settings import BASE_DIR
import polib #RECORDAR METER EN EL REQUIREMENTS DE HEROKU!!!!

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

    if (lang != en ): 
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

