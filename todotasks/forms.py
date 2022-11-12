from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django import forms
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placehoder': 'Add new task.....'}))
    body = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':20, 'cols':80})),
    
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['creator']
        

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

# class UserForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = '__all__'
