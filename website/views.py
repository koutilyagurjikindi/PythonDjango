from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def new_welcome(request):
    return HttpResponse("Welcome to Koutilya")

def date(request):
    return HttpResponse("Today data "+str(datetime.now()))

def about(request):
    return HttpResponse('I, am koutilya. And I started learning code')