from email.policy import default
from enum import unique
from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.


# class User(AbstractUser):
#     name = models.CharField(max_length= 200, null=True)
#     email = models.EmailField(unique=True, null=True)
    #username = models.CharField(max_length=50, null=True)


    #USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = []



class Todo(models.Model):
    creator = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    title = models.CharField(max_length = 200)
    body = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = [ '-updated', '-created']

    def __str__(self):
        return f'{self.title}: {self.creator}'
