from django.shortcuts import render, redirect
from .models import Messages, Room
from .forms import RoomForm

# Create your views here.


def homeView(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def roomView(request, pk):

    
    context={}
    return render(request,'base/room.html',context)




def createRoomView(request):

    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/create_room.html', context)



def updateRoomView(request, pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    if request.method == 'POST':
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/create_room.html',context)
