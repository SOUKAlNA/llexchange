from django.shortcuts import render
from django.shortcuts import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import *
from llexchange.models import Message, Profile

#Services may apper elementary since forms and templates are not implemented yet
#-------------------------------------------------------------
#USER SERVICE: 

class UserService():
    def user_login(self, request):
        username = request.GET.get("username","")
        password = request.GET.get("password","")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Logged in")  
        else:
            return HttpResponse("Invalid username or password")

    def user_logout(self, request):
        logout(request)
        return HttpResponse("Logged out")

    #New user sign in
    def user_register(self, request):
        username = request.GET.get("username","")
        password = request.GET.get("password","")
        email = request.GET.get("email","")
        is_staff = request.GET.get("is_staff","")
        if User.objects.filter(username=username).count()>0:
            return HttpResponse("Username taken")
        if User.objects.filter(email=email).count()>0:
            return HttpResponse("Invalid Email: already exists")
        #Create new user
        user = User.objects.create_user(username=username,password=password, email=email, is_staff=is_staff)
        user.save()
        #Login the newly registered user
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponse("Successfully signed in")

#-------------------------------------------------------------
#RATING SERVICE
 
class RatingService():
    class Meta():
        model= Profile
        exclude= ['created', 'firstname', 'lastname']
    
    def ComputeAvgRating(self, newRating):
        self.rating= (self.rating+newRating)//2
        return True

#-------------------------------------------------------------
#BLOCKING SERVICE

class DisscusionService():

    def isBlocked(self, c_username, t_username):
        blocked_users = User.objects.get(username=c_username).blocked_users.users.all()
        if t_username in blocked_users: 
            return True
  
#-------------------------------------------------------------
