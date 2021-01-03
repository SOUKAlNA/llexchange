from rest_framework import serializers
from .models import User, Moderator, Message, Comment, Reply, Profile, Language

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= {'username'}

class ModeratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderator
        fields=  {'username', 'firstname', 'lastname', 'mod_language'}

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields=  {'content', 'creator', 'created', 'closed'}

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields= {'content', 'creator', 'created', 'likes'}

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields= {'replyto', 'content', 'creator', 'created'}

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields= {'username', 'firstname', 'lastname', 'rating'}

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields= '__all__'
