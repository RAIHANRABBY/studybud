from django.urls import path
from .views import homeView, roomView, createRoomView, updateRoomView, deleteRoomView, loginpage, logoutpage, registerpage, deleteMsg
from . import views
urlpatterns = [
    path('home/', homeView, name='home'),
    path('activity/', views.activityView, name='activity'),
    path('topics/', views.topicsView, name='topics'),
    path('', homeView, name='home'),
    path('room/<str:pk>', roomView, name='room'),
    path('createroom/', createRoomView, name='create_room'),
    path('updateroom/<str:pk>', updateRoomView, name='update-room'),
    path('deleteroom/<str:pk>', deleteRoomView, name='delete-room'),
    path('login/', loginpage, name='login'),
    path('logout/', logoutpage, name='logout'),
    path('register/', registerpage, name='register'),
    path('msg_d/<int:pk>', deleteMsg, name='delete_msg'),
    path('profile/<int:pk>', views.profileView, name='profile'),
    path('edit-profile/<int:pk>', views.editProfile, name='edit-profile'),

]
