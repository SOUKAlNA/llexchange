from django.contrib.auth import login
from django.views.generic import CreateView
from .models import User, Moderator, Message, Comment, Reply, Profile, Language
from .Services import RatingService, DisscusionService, UserService
from django.urls import path
from django.shortcuts import render
from rest_framework.response import Response
from .Serializers import UserSerializer, MessageSerializer, ModeratorSerializer, CommentSerializer, ReplySerializer, ProfileSerializer, LanguageSerializer, RatingSerializer
from rest_framework.decorators import api_view


#Views is Django represent Controllers (whereas Templates represent the Views in the MVC architecture)
#The rest of the Views requires the views templates and corresponding forms to be implemented

#-------------------------------------------------------------
#pylint: disable=no-member

#Get languages of the platform
@api_view(['GET'])
def LanguageList(request):
    languages= Language.objects.all()
    serializer= LanguageSerializer(languages, many=True)
    return Response(serializer.data)

#pylint: disable=no-member
#Get tutors of a language
@api_view(['GET'])
def TutorsList(request, pk):
    tutors= Language.objects.get(id=pk)
    serializer= LanguageSerializer(tutors, many=True)
    return Response(serializer.data)

#Get of a under a language
@api_view(['GET'])
def MessagesList(request, pk):
    messages= Language.objects.get(id=pk)
    serializer= LanguageSerializer(messages, many=True)
    return Response(serializer.data)

#pylint: disable=no-member
#Get profile of a tutor
@api_view(['GET'])
def TutorProfile(request, pk):
    profile= Profile.objects.get(id=pk)
    serializer= ProfileSerializer(profile, many=True)
    return Response(serializer.data)

#Post a message
@api_view(['POST'])
def PostMessage(request):
    serializer= MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response('Posted')

#Post a comment
@api_view(['POST'])
def PostComment(request):
    serializer= CommentSerializer(data=request.data)
    if serializer.is_valid():
        if DisscusionService.isBlocked:
            return Response("You cannot post in this discussion.")
        else:
            serializer.save()
            return Response('Posted')

#Post a reply
@api_view(['POST'])
def PostReply(request):
    serializer= ReplySerializer(data=request.data)
    if serializer.is_valid():
        if DisscusionService.isBlocked:
            return Response("You cannot post in this discussion.")
        else:
            serializer.save()
            return Response('Posted')

#Rate tutor's response
@api_view(['POST'])
def RateTutor(request):
    serializer= ProfileSerializer(data=request.data)
    profile= Profile.objects.get(id=request.data.pk)
    if serializer.is_valid(): 
        if RatingService.ComputeAvgRating(profile, serializer.validated_data.pop('rating')):
            serializer.update()
            return Response("Your rating has been recorded.")

#Close discussion
@api_view(['POST'])
def CloseDiscussion(request):
    serializer= MessageSerializer(data=request.data)
    if serializer.is_valid(): 
        serializer.__setattr__('closed', True)
        serializer.update()
        return Response("The discussion has been closed.")

#Tutor creates a profile
@api_view(['POST'])
def CreateProfile(request):
    serializer= ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response('Profile created')

#Delete User/Tutor
@api_view(['DELETE'])
def DeleteUser_Tutor(request):
    user= User.objects.get(id=request.data.pk)
    user.delete()
    return Response('User deleted')

#Delete Message
@api_view(['DELETE'])
def DeleteMessage(request):
    message= Message.objects.get(id=request.data.pk)
    message.delete()
    return Response('Message deleted')

#Delete Comment
@api_view(['DELETE'])
def DeleteComment(request):
    comment= Comment.objects.get(id=request.data.pk)
    comment.delete()
    return Response('Comment deleted')

#Delete Reply
@api_view(['DELETE'])
def DeleteReply(request):
    reply= Reply.objects.get(id=request.data.pk)
    reply.delete()
    return Response('Reply deleted')
