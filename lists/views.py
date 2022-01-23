from pickle import GET
from django.http import response
from django.shortcuts import render,redirect
from django.template import context
from django.contrib.auth import login
from rest_framework.decorators import action, api_view
from django.contrib import messages
from .forms import UserForm,ItemForm,ListForm
from django.contrib.auth.models import User
from .serialzers import allSerailizer,allItemSerailizer,allListSerailizer
from rest_framework.response import Response
from .models import Item,List

# Create your views here.
@api_view(['GET'])
def allusers(request):
    users = User.objects.all()
    serailizer = allSerailizer(users,many=True)
    return Response(serailizer.data)
    
@api_view(['GET'])
def allitems(request):
    items = Item.objects.all()
    serailizer = allItemSerailizer(items,many=True)
    return Response(serailizer.data)

@api_view(['GET'])
def alllists(request):
    lists = List.objects.all()
    serailizer = allListSerailizer(lists,many=True)
    return Response(serailizer.data)


def register(request):
    if request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration successful.")
            return redirect('/list/allusers/')
        messages.error(request,"Unsuccessful registration. Invalid information .")
    form = UserForm()
    return render (request=request, template_name="register.html",context={"register_form":form})

def login(request):
    return

def editProfile(request,pk):
    action = 'update'
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)

    if request.method =='POST':
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('/list/profile/'+str(user.id))
    context = {'action':action, 'form':form}
    return render(request,'register.html',context)
@api_view(['GET'])
def profile(request,pk):
    user = User.objects.get(id=pk)
    serializers = allSerailizer(user,many=False)
    return Response(serializers.data)

def deleteUser(request,pk):
    return 

def addItem(request):
    if request.method =="POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Item Added Sucessfully.")
            return redirect('/list/all_items/')
        messages.error(request,"Invalid Information .Item could not be added .")
    form = ItemForm()
    context ={'action':action,'form':form}
    return render(request,'additem.html',context)

@api_view(['GET'])
def item(request,pk):
    aitem = Item.objects.get(id=pk)
    serializers = allItemSerailizer(aitem,many=False)
    return Response(serializers.data)

@api_view(['GET'])
def listItems(request):
    return

def editItem(request,pk):
    action ='update'
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)

    if request.method =='POST':
        form = ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/list/item/'+str(item.id))

    context = {'action':action, 'form':form}
    return render(request,'additem.html',context)


def deleteItem(request,pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect('/list/allitems/')

def addlist(request):
    if request.method =="POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"List Added Sucessfully.")
            return redirect('/list/all_lists/')
        messages.error(request,"Invalid Information .List could not be added .")
    form = ListForm()
    context ={'action':action,'form':form}
    return render(request,'addlist.html',context)


@api_view(['GET'])
def list(request,pk):
    alist = List.objects.get(id=pk)
    serializers = allListSerailizer(alist,many=False)
    return Response(serializers.data)


@api_view(['GET'])
def userLists(request):
    return

def editList(request,pk):
    action ='update'
    list = List.objects.get(id=pk)
    form = UserForm(instance=list)

    if request.method =='POST':
        form = UserForm(request.POST,instance=list)
        if form.is_valid():
            form.save()
            return redirect('/list/list/'+str(list.id))

    context ={'action':action,'form':form}
    return render(request,'addlist.html',context)

def deleteList(request,pk):
    list = List.objects.get(id=pk)
    items = Item.objects.filter(List_id=pk)
    items.delete()
    list.delete()
    return redirect('/list/alllists/')