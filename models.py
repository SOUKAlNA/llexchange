# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import (GenericForeignKey, GenericRelation)
from django.contrib.contenttypes.models import ContentType

#-------------------------------------------------------------
#User Entity

class User(models.Model):
    email = models.EmailField(max_length=50)
    username= models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    #To differentiate tutors from regular users (specific to Django)
    is_staff  = models.BooleanField(default=False)
    #To report user's account
    flag= models.BooleanField()

    #pylint: disable=no-member
    def __str__(self):
        return self.username

#-------------------------------------------------------------
#Profile Entity

class Profile(models.Model):
    tutor_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    username= models.CharField(max_length=50)
    firstname= models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    rating= models.IntegerField()
    #To report tutor's account
    flag= models.BooleanField()

#-------------------------------------------------------------
#Moderator Entity

class Moderator(models.Model):
    email = models.EmailField(max_length=50)
    username= models.CharField(max_length=50)
    firstname= models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    mod_language= models.CharField(max_length=50)
#-------------------------------------------------------------
#Message Entity:

class Message(models.Model):
    content = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    #To report a user's message
    flag= models.BooleanField(blank=True, default=False)
    closed = models.BooleanField(blank=True, default=False)

    class Meta:
        get_latest_by = "-pk"

class Comment(models.Model):
    content = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    message= models.ForeignKey(Message, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = GenericRelation('Like')
    #To report a tutor's comment 
    flag= models.BooleanField()
    
    #pylint: disable=no-member
    def like(self, user):
        return self.likes.create(user=user)
    
    def __str__(self):
        return self.creator.username

class Reply(models.Model):
    replyto = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    replies= models.ForeignKey(Comment, on_delete=models.CASCADE)
    #To report a user"s or tutor's reply
    flag= models.BooleanField()
    #pylint: disable=no-member
    def __str__(self):
        return self.creator.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    obj_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'obj_id')

#-------------------------------------------------------------
#Language Entity

class Language(models.Model):
    language_name= models.CharField(max_length=50)
    messages = models.ForeignKey(Message, null=True, on_delete=models.CASCADE)
    tutors= models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    moderators= models.ForeignKey(Moderator, null=True, on_delete=models.CASCADE)
    #creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    
    #pylint: disable=no-member
    def __str__(self):
        return self.tutors.username
    

#-------------------------------------------------------------
#Rating Entity

class Rating(models.Model):
    rating_int= models.IntegerField()
    rated_tutor= models.ForeignKey(User, null=True, on_delete=models.CASCADE)

#-------------------------------------------------------------
#Blocked Users
class Blocked(models.Model):
    user = models.ForeignKey(User, related_name="blocked_users", null=True, on_delete=models.CASCADE)
    userb = models.ManyToManyField(User, related_name="blocked_by")

#-------------------------------------------------------------
#Reported Users
class Reported(models.Model):
    reported_user = models.ForeignKey(User, related_name="reported_user", null=True, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name="reported_by")
    reported_post = models.ManyToManyField(Message, null=True, related_name="reported_post")
    reported_comment = models.ManyToManyField(Comment, null=True, related_name="reported_comment")
    reported_reply = models.ManyToManyField(Reply, null=True, related_name="reported_reply")
