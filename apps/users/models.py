from __future__ import unicode_literals
from ..login_reg.models import User, Friend, UserManager
from django.db import models

class MessageManager(models.Manager):
    def addUser(self, content, id, poster):
        user = User.objects.get(id=id)
        poster = User.objects.get(id=poster)
        self.create(content=content, user_id=user, poster=poster)

class CommentManager(models.Manager):
    def addComment(self, content, poster, message_id):
        poster = User.objects.get(id=poster)
        message = Message.objects.get(id=message_id)
        self.create(content=content, user_id=poster, message_id=message)

# Create your models here.
class Message(models.Model):
    content = models.TextField()
    poster = models.ForeignKey(User, related_name='poster')
    user_id = models.ForeignKey(User, related_name='user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    messageManager = MessageManager()
    objects = models.Manager()

class Comment(models.Model):
    content = models.TextField()
    user_id = models.ForeignKey(User)
    message_id = models.ForeignKey(Message)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    commentManager = CommentManager()
    objects = models.Manager()
