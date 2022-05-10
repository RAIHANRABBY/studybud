from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import Messages, Room, Topic
from .forms import RoomForm

# Create your views here.

# this is the home page view


def homeView(request):
    # getting the data that is passed on the query from home page tamplate
    q = request.GET.get('q') if request.GET.get('q') != None else ''
# the ways the search option will work
    rooms = Room.objects.filter(Q(topic__name__icontains=q) |
                                Q(name__icontains=q) |
                                Q(describtion__icontains=q)



                                )

    topic = Topic.objects.all()
    room_count= rooms.count()
    context = {"rooms": rooms, 'topic': topic,'room_count':room_count}
    return render(request, "base/home.html", context)


def roomView(request, pk):

    context = {}
    return render(request, 'base/room.html', context)



@login_required(login_url='login')
def createRoomView(request):

    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/create_room.html', context)

# update the room
# taking the primary key of the room that we want to update


def updateRoomView(request, pk):
    # get the room that matches with the primary key
    room = Room.objects.get(id=pk)
    # create a form that has the instance of the room
    form = RoomForm(instance=room)
    #redirecting the other user from using the updating option of a user
    if request.user != room.host:
        return redirect('home')
    if request.method == 'POST':
        # updating new data that has the same instance as room
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/create_room.html', context)


# Delete the room
def deleteRoomView(request, pk):
    room = Room.objects.get(id=pk)
    #redirecting the other user from using the delete option of a user
    if request.user != room.host:
        return redirect('home')
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    context = {'obj': room}
    return render(request, 'base/delete.html', context)






def loginpage(request):


    if request.user.is_authenticated:
        return redirect('home')


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')
        
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)  
            return redirect('home')


        else:
            messages.error(request, 'Wrong Username or password.')

    

    context={}

    return render(request,'base/login.html',context)


def logoutpage(request):
    logout(request)
    return redirect('login')