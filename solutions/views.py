from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

def hello(request):
    return HttpResponse("Hello world, Django.")