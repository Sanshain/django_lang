# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.utils.translation import ugettext as _

# Create your views here.

def index(request):

##    from django.utils import translation
##    user_language = 'ru'
##    translation.activate(user_language)
##    request.session[translation.LANGUAGE_SESSION_KEY] = user_language

    val = _(u"мир")
    val = _(u"Hello World!")
    return HttpResponse(val)



# https://vivazzi.pro/it/translate-django/

lang = lambda request: render(request, "lang.html")


