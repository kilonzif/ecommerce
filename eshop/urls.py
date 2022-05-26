from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [

   # search_users 

    #slash, name of function (views.py), name 
    path('',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.login_user, name='login') ,   
    path('logout/',views.logout_user, name='logout'),
     
    path('/product/<int:id>',views.view_product,name='view_product')

]
