from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# creating a class for the topic


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# model for room


class Room(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)

    # time of update and delete the room
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    # to use the ordering. ordering the posts
    class Meta:
        ordering = ['-update', '-create']

    def __str__(self):
        return self.name


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    p_pic = models.ImageField(upload_to='none',default='default.jpg')
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'
