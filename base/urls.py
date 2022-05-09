from django.urls import path
from .views import homeView, roomView, createRoomView, updateRoomView

urlpatterns = [
    path('home/', homeView, name='home'),
    path('', homeView),
    path('room/<str:pk>', roomView, name='room'),
    path('createroom/', createRoomView, name='create_room'),
    path('updateroom/<str:pk>', updateRoomView, name='update-room'),

]
