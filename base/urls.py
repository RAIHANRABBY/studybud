from django.urls import path
from .views import  homeView, roomView, createRoomView, updateRoomView, deleteRoomView,loginpage,logoutpage

urlpatterns = [
    path('home/', homeView, name='home'),
    path('', homeView,name='home'),
    path('room/<str:pk>', roomView, name='room'),
    path('createroom/', createRoomView, name='create_room'),
    path('updateroom/<str:pk>', updateRoomView, name='update-room'),
    path('deleteroom/<str:pk>', deleteRoomView, name='delete-room'),
    path('login/', loginpage, name='login'),
    path('logout/', logoutpage, name='logout'),

]
