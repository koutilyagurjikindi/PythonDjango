from django.shortcuts import render,get_object_or_404,redirect
from django.forms import modelform_factory
from .models import Meeting,Room
# Create your views here.
def detail(request,id):
    print(id,"dlkfdlfkldkf")
    meeting=get_object_or_404(Meeting,pk=id)
    return render(request,'meetings/detail.html',{'meeting':meeting})

def roomdetail(request):
    room=Room.objects.all()
    return render(request,'meetings/roomdetail.html',{'rooms':room})

Meetingform = modelform_factory(Meeting,exclude=[])

def new(request):
    if request.method=="POST":
        form = Meetingform(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('new_welcome')
    else:
        form = Meetingform()
    return render(request,'meetings/new.html',{'form':form})