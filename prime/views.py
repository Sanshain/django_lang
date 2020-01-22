# -*- coding: utf-8 -*-
from __future__ import unicode_literals

##from django.shortcuts import render
from django.http import HttpResponse

from django.utils.translation import ugettext as _

# Create your views here.

def index(request):
    val = _(u"мир")
    val = _(u"Hello World!")
    return HttpResponse(val)

