from django.shortcuts import render, HttpResponse 
from gymkhana.utils import check_response, trans_keyword
# Create your views here.

_ = lambda s: s

def start(request): 

    return render(request, 'start.html')

def game_1(request): 
    # diagrama de actividades
    return render(request, 'game_1.html')

def game_2(request): 
    # Diagrama de casos de uso
    return render(request, 'game_2.html')

def game_3(request): 
    #  Object Diagrams
    return render(request, 'game_3.html')


def response_1(request): 

    key = _('nal hutta')
    lang = request.LANGUAGE_CODE
    keyword = request.GET['keyword']
    keyword = trans_keyword(keyword, lang)
    template = check_response(key, keyword)

    return render(request, template)

def response_2(request): 

    key = _('fight zombies')
    lang = request.LANGUAGE_CODE
    keyword = request.GET['keyword']
    keyword = trans_keyword(keyword, lang)
    template = check_response(key, keyword)

    return render(request, template)

def response_3(request): 

    key = _('no humans')
    lang = request.LANGUAGE_CODE
    keyword = request.GET['keyword']
    keyword = trans_keyword(keyword, lang)
    template = check_response(key, keyword)

    return render(request, template)