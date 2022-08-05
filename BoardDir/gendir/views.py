from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import default_storage
from django.template import loader
from django.urls import reverse

from .models import Persons, Positions, Task_types, Tasks


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
