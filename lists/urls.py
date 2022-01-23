from ast import Delete
from os import name
from django.urls import path
from django.urls.resolvers import URLPattern

from .import views

urlpatterns =[
    #-------------TESTS-----------------------
    path('allusers/',views.allusers,name="all_users"),
    path('all_items/',views.allitems,name="all_items"),
    path('all_lists/',views.alllists,name="all_lists"),
    #-------------USERS-----------------------
     path('register/',views.register,name='register_user'),
     path('login/',views.login,name='login_user'),
     path('edit_profile/<str:pk>/',views.editProfile,name='Edit_Profile'),
     path('profile/<str:pk>/',views.profile,name='Profile'),
    #-------------ITEMS-----------------------
     path('add_item/',views.addItem,name='add_item'),
     path('item/<str:pk>/',views.item,name='Specific_Item'),
     path('list_items/<str:pk>/',views.listItems,name='List_Items'),
     path('edit_item/<str:pk>/',views.editItem,name='Edit_Item'),
     path('delete_item/<str:pk>/',views.deleteItem,name='Delete_Item'),
    #-------------LISTS-----------------------
     path('add_list/',views.addlist,name='add_list'),
     path('list/<str:pk>/',views.list,name='Specific_List'),
     path('user_lists/<str:pk>/',views.userLists,name='User_Lists'),
     path('edit_list/<str:pk>/',views.editList,name='Edit_List'),
     path('delete_list/<str:pk>/',views.deleteList,name='Delete_List'),  
]