from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting

# Create your views here.
def new_welcome(request):
    return render(request,"website/welcome.html",{'meetings':Meeting.objects.all()})

def date(request):
    return HttpResponse("Today data "+str(datetime.now()))

def about(request):
    return HttpResponse('I, am koutilya. And I started learning code')