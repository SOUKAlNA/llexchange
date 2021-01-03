from django.contrib import admin

# Register your models here.
from .models import User, Moderator, Message, Comment, Reply, Profile, Language

admin.site.register(User)
admin.site.register(Moderator)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Profile)
admin.site.register(Language)