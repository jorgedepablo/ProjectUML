"""ProjectUML URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ProjectUML.views import home
from gymkhana.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('start/', start),
    path('game-1/', game_1),
    path('response-1/', response_1),
    path('game-2/', game_2),
    path('response-2/', response_2),
    path('game-3/', game_3),
    path('response-3/', response_3)
]
