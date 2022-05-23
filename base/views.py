from django.shortcuts import render, redirect
from django.db.models import Q
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Messages, Room, Topic,Profile
from .forms import RoomForm, UserRegister,UserUpdate

# Create your views here.

# this is the home page view


def homeView(request):
    # getting the data that is passed on the query from home page tamplate
    q = request.GET.get('q') if request.GET.get('q') != None else ''
# the ways the search option will work
    rooms = Room.objects.filter(Q(topic__name__icontains=q) |
                                Q(name__icontains=q) |
                                Q(description__icontains=q)



                                )

    topic = Topic.objects.all()
    
    room_count = rooms.count()
  
    msg = Messages.objects.filter(
        Q(room__topic__name__icontains=q)).order_by('-create')[0:5]
    context = {"rooms": rooms, 'topic': topic,
               'room_count': room_count, 'msg': msg,
               
            
               }
    return render(request, "base/home.html", context)


# profile of the user

def profileView(request, pk):
    user = User.objects.get(id=pk)
    # access the children from the parents model
    room = user.room_set.all()
    msg = user.messages_set.all()
    topic = Topic.objects.all()
    profile=Profile.objects.get(user=user.id)

    
    room_count=len(room)
    profile_status=True
    content = {'rooms': room, 'msg': msg, 'user': user, 
                'topic': topic,'room_count':room_count,
                'profile':profile_status,'user_profile':profile}
    return render(request, 'base/profile.html', content)



@login_required(login_url='login')
def editProfile(request,pk):
    user=User.objects.get(id=pk)
   
    form=UserUpdate(instance=user)
    if request.user != user:
        return redirect('home')
    if request.method == 'POST':
        form= UserUpdate(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk= user.id)
    context={'form':form}
    return render(request,'base/edit-profile.html',context)


def roomView(request, pk):
    room = Room.objects.get(id=pk)
    room_message = room.messages_set.all().order_by('create')
    participants = room.participants.all()
    # count of the number of perticipents of the room
    participants_count = len(participants)
    if request.method == 'POST':

        msg = Messages.objects.create(
            user=request.user, room=room, body=request.POST.get('comment'))
        # adding the participants that masseged on the room
        room.participants.add(request.user)

        return redirect('room', pk=room.id)

    context = {'msg': room_message, 'room': room, 'participants': participants,
               'p_count': participants_count

               }
    return render(request, 'base/room.html', context)


@login_required(login_url='login')
def createRoomView(request):

    form = RoomForm()
    topic=Topic.objects.all()

    create_of_room=True
    if request.method == 'POST':
        room_topic = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=room_topic)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description')

        )
        return redirect('home')
    context = {'form': form,'topic': topic,'create':create_of_room}
    return render(request, 'base/create_room.html', context)

# update the room
# taking the primary key of the room that we want to update


def updateRoomView(request, pk):
    # get the room that matches with the primary key
    room = Room.objects.get(id=pk)
    # create a form that has the instance of the room
    form = RoomForm(instance=room)
    # redirecting the other user from using the updating option of a user
    if request.user != room.host:
        return redirect('home')
    if request.method == 'POST':
        room_topic = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=room_topic)
        # updating new data that has the same instance as room
        room.name = request.POST.get('name')
        room.topic=topic
        room.description=request.POST.get('description')
        room.save()
        
        return redirect('home')
    context = {'form': form,'room':room}
    return render(request, 'base/create_room.html', context)


# Delete the room
def deleteRoomView(request, pk):
    room = Room.objects.get(id=pk)
    # redirecting the other user from using the delete option of a user
    if request.user != room.host:
        return redirect('home')
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    context = {'obj': room}
    return render(request, 'base/delete.html', context)


def loginpage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Wrong Username or password.')

    context = {'page': page}

    return render(request, 'base/login_register.html', context)


def logoutpage(request):
    logout(request)
    return redirect('login')


def registerpage(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, user.first_name +
                             ' your account is created successfully.')
            return redirect('home')
        else:
            form = UserRegister()
            messages.error(
                request, 'Error occurred. please enter details carefully.')

    context = {'form': form}
    return render(request, 'base/login_register.html', context)


@login_required(login_url='home')
def deleteMsg(request, pk):
    msg = Messages.objects.get(id=pk)
    # redirecting the other user from using the delete option of a user
    if request.user != msg.user:
        return redirect('home')
    if request.method == 'POST':
        msg.delete()
        return redirect('home')

    context = {'obj': msg}
    return render(request, 'base/delete.html', context)
