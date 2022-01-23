import email
from pyexpat import model
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Item,List
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","password1","password2")

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class ListForm(ModelForm):
    class Meta:
        model = List
        fields ='__all__'