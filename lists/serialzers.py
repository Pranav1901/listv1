from django.forms import models
from rest_framework import fields, serializers
from .models import List,Item
from django.contrib.auth.models import User



class allSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=("first_name","last_name","username","email")

class allItemSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields ='__all__'

class allListSerailizer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields ='__all__'
        depth = 1