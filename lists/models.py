from ast import Delete
import email
from operator import mod
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):

    title = models.CharField(max_length=30,null=False)
    completed = models.BooleanField(default=False)
    added_by = models.ForeignKey(User,on_delete=Delete,null=False)
    added_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.title

class List(models.Model):
    name = models.CharField(max_length=30,null=False)
    discription = models.CharField(max_length=100,null=True)
    created_by = models.ForeignKey(User,on_delete=Delete,null=False)
    shared_with = models.ManyToManyField(User,related_name='shared')
    items = models.ManyToManyField(Item)
    date = models.DateTimeField(auto_now_add=True,null=False,blank=False)

    def __str__(self):
        return self.name

